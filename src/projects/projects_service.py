import os
from typing import List, Optional, Sequence
from uuid import uuid4
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from projects.projects_data import ProjectEntity, ProjectModel, ProjectCreate, ProjectUpdate, to_model, to_entity
from utils import sanitize_folder_name


class ProjectsService:

    async def _get_all_projects(self, session: AsyncSession, enabled_only: bool = False) -> Sequence[ProjectEntity]:
        query = select(ProjectEntity)
        if enabled_only:
            query = query.where(ProjectEntity.enabled == True)

        result = await session.execute(query)
        return result.scalars().all()

    async def _get_project_entity_by_id(self, session: AsyncSession, project_id: str) -> Optional[ProjectEntity]:
        result = await session.execute(
            select(ProjectEntity).where(ProjectEntity.id == project_id)
        )
        return result.scalars().first()

    async def get_all_projects(self, session: AsyncSession, enabled_only: bool = False) -> List[ProjectModel]:
        """Get all projects, optionally filtering by enabled status"""
        entities = await self._get_all_projects(session, enabled_only)
        return [to_model(entity) for entity in entities]

    async def get_project_by_id(self, session: AsyncSession, project_id: str) -> Optional[ProjectModel]:
        """Get a project by its ID"""
        entity = await self._get_project_entity_by_id(session, project_id)
        return to_model(entity) if entity else None
    
    async def create_project(self, session: AsyncSession, project_create: ProjectCreate) -> ProjectModel:
        """Create a new project"""
        
        # Usa il percorso assoluto alla root del progetto invece del percorso relativo al file
        project_folder = os.path.join(
            'data/projects', 
            sanitize_folder_name(project_create.name)
        )
        
        # Assicurati che la directory esista
        os.makedirs(os.path.dirname(project_folder), exist_ok=True)

        project = ProjectModel(
            id=str(uuid4()),
            name=project_create.name,
            description=project_create.description,
            project_folder=project_folder,
            creation_date=datetime.now(),
            update_date=datetime.now(),
            enabled=True,
            disabled_date=None
        )
            
        entity = to_entity(project)
        
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return to_model(entity)
    
    async def update_project(self, session: AsyncSession, project_id: str, project_update: ProjectUpdate) -> Optional[ProjectModel]:
        """Update an existing project"""
        entity = await self._get_project_entity_by_id(session, project_id)
        if not entity:
            return None
        
        # Update fields
        entity.name = project_update.name
        entity.description = project_update.description
        # update_date will be automatically updated by SQLAlchemy's onupdate
        
        await session.commit()
        await session.refresh(entity)
        return to_model(entity)
    
    async def disable_project(self, session: AsyncSession, project_id: str) -> Optional[ProjectModel]:
        """Disable a project (soft delete)"""
        entity = await self._get_project_entity_by_id(session, project_id)
        if not entity:
            return None
        
        entity.enabled = False
        entity.disabled_date = datetime.now()
        
        await session.commit()
        await session.refresh(entity)
        return to_model(entity)
    
    async def enable_project(self, session: AsyncSession, project_id: str) -> Optional[ProjectModel]:
        """Enable a previously disabled project"""
        entity = await self._get_project_entity_by_id(session, project_id)
        if not entity:
            return None
        
        entity.enabled = True
        entity.disabled_date = None
        
        await session.commit()
        await session.refresh(entity)
        return to_model(entity)


# Singleton instance
projects_service = ProjectsService()