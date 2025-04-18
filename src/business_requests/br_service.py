import os
from typing import List, Optional, Sequence
from uuid import uuid4
from datetime import datetime

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile

from business_requests.br_data import (
    BusinessRequestEntity,
    BusinessRequestModel,
    BusinessRequestCreate,
    BusinessRequestEvaluationResult,
    to_model,
    to_entity
)
from business_requests.br_evaluator.crew import create_br_evaluator_crew
from projects.projects_service import projects_service


class BusinessRequestService:

    async def _get_version_entity_by_id(self, session: AsyncSession, br_id: str) -> Optional[BusinessRequestEntity]:
        """Get a specific version of a business request by its ID"""
        result = await session.execute(
            select(BusinessRequestEntity).where(BusinessRequestEntity.id == br_id)
        )
        return result.scalars().first()

    async def _get_versions_entity_by_project_id(self, session: AsyncSession, project_id: str) -> Sequence[BusinessRequestEntity]:
        query = select(BusinessRequestEntity).where(
            BusinessRequestEntity.project_id == project_id
        ).order_by(
            desc(BusinessRequestEntity.creation_date)
        )
        result = await session.execute(query)
        return result.scalars().all()

    async def get_versions_by_project_id(self, session: AsyncSession, project_id: str) -> List[BusinessRequestModel]:
        """Get all versions of a business request for a project, ordered by most recent first"""
        entities = await self._get_versions_entity_by_project_id(session, project_id)
        return [to_model(entity) for entity in entities]
    
    async def get_version_by_id(self, session: AsyncSession, br_id: str) -> Optional[BusinessRequestModel]:
        """Get a specific version of a business request by its ID"""
        entity = await self._get_version_entity_by_id(session, br_id)
        return to_model(entity) if entity else None
    
    async def create_version(self, session: AsyncSession, br_upload: BusinessRequestCreate, file: UploadFile) -> BusinessRequestModel:
        """Create a new version of a business request with an uploaded markdown file"""
        # Verify that the project exists
        project = await projects_service.get_project_by_id(session, br_upload.project_id)
        if not project:
            raise ValueError(f"Project with ID {br_upload.project_id} not found")

        # Get the latest version number for this project
        query = select(BusinessRequestEntity).where(
            BusinessRequestEntity.project_id == br_upload.project_id
        ).order_by(desc(BusinessRequestEntity.version))

        result = await session.execute(query)
        latest_entity = result.scalars().first()
        
        # Determine the new version number
        new_version = 1 if not latest_entity else latest_entity.version + 1
        
        # If this is a new version, deactivate all previous versions
        if latest_entity:
            # Query to get all versions for this project
            active_versions_query = select(BusinessRequestEntity).where(
                BusinessRequestEntity.project_id == br_upload.project_id,
                BusinessRequestEntity.is_active == True
            )
            active_versions_result = await session.execute(active_versions_query)
            active_versions = active_versions_result.scalars().all()
            
            # Deactivate all previous active versions
            for version in active_versions:
                version.is_active = False
            
            await session.flush()
        
        # Create upload directory if it doesn't exist
        upload_dir = os.path.join(os.getcwd(), project.project_folder, 'upload')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Generate a unique filename
        filename = f"br_v{new_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        file_path = os.path.join(upload_dir, filename)
        
        # Save the file
        content = await file.read()
        with open(file_path, 'wb') as f:
            f.write(content)
        
        # Store the relative path from project folder
        relative_path = os.path.join('upload', filename)
        
        # Create a new BusinessRequestModel
        business_request = BusinessRequestModel(
            id=str(uuid4()),
            project_id=br_upload.project_id,
            version=new_version,
            file_path=relative_path,
            creation_date=datetime.now(),
            is_active=True  # New version is active by default
        )
        
        entity = to_entity(business_request)
        
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return to_model(entity)
    
    async def get_file_content(self, session: AsyncSession, br_id: str) -> Optional[str]:
        """Get the content of a business request markdown file"""
        br = await self.get_version_by_id(session, br_id)
        if not br:
            return None

        prj = await projects_service.get_project_by_id(session, br.project_id)
        if not prj:
            return None
            
        # Construct the full path to the file
        file_path = os.path.join(
            os.getcwd(),
            prj.project_folder,
            br.file_path
        )
        
        # Check if file exists
        if not os.path.exists(file_path):
            return None
            
        # Read and return the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return content
    
    async def create_br_evaluation(self, session: AsyncSession, br_id: Optional[str] = None, force_evaluation: bool = False) -> Optional[BusinessRequestEvaluationResult]:

        br = await self.get_version_by_id(session, br_id)
        if not br:
            return None

        prj = await projects_service.get_project_by_id(session, br.project_id)
        if not prj:
            return None

        br_content = await self.get_file_content(session, br_id)
        if not br_content:
            return None

        output_file_path = f"{prj.project_folder}/output/br_v{br.version}_evaluation.json"

        evaluator_crew = create_br_evaluator_crew(output_file_path=output_file_path)

        result = evaluator_crew.kickoff(inputs={
            "business_request": br_content
        })

        return result.pydantic

    async def received_answers(self):
        pass


# Singleton instance
br_service = BusinessRequestService()
