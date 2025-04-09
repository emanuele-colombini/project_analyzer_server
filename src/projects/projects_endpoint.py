from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database_manager import database_manager
from projects.projects_data import ProjectModel, ProjectCreate, ProjectUpdate
from projects.projects_service import projects_service

router = APIRouter(
    prefix='/projects'
)


async def get_db():
    """Dependency for database session"""
    async with database_manager.AsyncSessionFactory() as session:
        yield session


@router.get("", response_model=List[ProjectModel])
async def get_all_projects(enabled_only: bool = False, db: AsyncSession = Depends(get_db)):
    """Get all projects, optionally filtering by enabled status"""
    return await projects_service.get_all_projects(db, enabled_only=enabled_only)


@router.get("/{project_id}", response_model=ProjectModel)
async def get_project_by_id(project_id: str, db: AsyncSession = Depends(get_db)):
    """Get a project by its ID"""
    project = await projects_service.get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ProjectModel with ID {project_id} not found"
        )
    return project


@router.post("", response_model=ProjectModel, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    """Create a new project"""
    return await projects_service.create_project(db, project)


@router.put("/{project_id}", response_model=ProjectModel)
async def update_project(project_id: str, project: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    """Update an existing project"""
    updated_project = await projects_service.update_project(db, project_id, project)
    if not updated_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ProjectModel with ID {project_id} not found"
        )
    return updated_project


@router.patch("/{project_id}/disable", response_model=ProjectModel)
async def disable_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """Disable a project (soft delete)"""
    disabled_project = await projects_service.disable_project(db, project_id)
    if not disabled_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ProjectModel with ID {project_id} not found"
        )
    return disabled_project


@router.patch("/{project_id}/enable", response_model=ProjectModel)
async def enable_project(project_id: str, db: AsyncSession = Depends(get_db)):
    """Enable a previously disabled project"""
    enabled_project = await projects_service.enable_project(db, project_id)
    if not enabled_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ProjectModel with ID {project_id} not found"
        )
    return enabled_project

