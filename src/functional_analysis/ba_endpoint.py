from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from functional_analysis.ba_service import ba_service
from core.database_manager import database_manager

router = APIRouter(
    prefix='/functional_analysis'
)


async def get_db():
    """Dependency for database session"""
    async with database_manager.AsyncSessionFactory() as session:
        yield session


@router.post("/{br_id}")
async def create_analysis(br_id: str, db: AsyncSession = Depends(get_db)):

    return await ba_service.create_functional_analysis(db, br_id)
