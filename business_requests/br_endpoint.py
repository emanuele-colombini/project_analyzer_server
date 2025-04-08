from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from business_requests.br_evaluator.models import EvaluationResult
from core.database_manager import database_manager
from business_requests.br_data import BusinessRequestModel, BusinessRequestCreate
from business_requests.br_service import br_service

router = APIRouter(
    prefix='/business-requests'
)


async def get_db():
    """Dependency for database session"""
    async with database_manager.AsyncSessionFactory() as session:
        yield session


@router.get("/project/{project_id}/versions", response_model=List[BusinessRequestModel])
async def get_versions_by_project_id(project_id: str, db: AsyncSession = Depends(get_db)):
    """Get all versions of a business request for a project, ordered by most recent first"""
    return await br_service.get_versions_by_project_id(db, project_id)


@router.get("/{br_id}", response_model=BusinessRequestModel)
async def get_version_by_id(br_id: str, db: AsyncSession = Depends(get_db)):
    """Get a specific version of a business request by its ID"""
    business_request = await br_service.get_version_by_id(db, br_id)
    if not business_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Business Request with ID {br_id} not found"
        )
    return business_request


@router.post("", response_model=BusinessRequestModel, status_code=status.HTTP_201_CREATED)
async def create_version(br_create: BusinessRequestCreate, db: AsyncSession = Depends(get_db)):
    """Create a new version of a business request (automatically becomes the active version)"""
    return await br_service.create_version(db, br_create)


@router.post("/{br_id}/questions", response_model=EvaluationResult)
async def get_questions(br_id: str, db: AsyncSession = Depends(get_db)):
    """Get questions for a specific version of a business request"""
    return await br_service.get_questions(db, br_id)