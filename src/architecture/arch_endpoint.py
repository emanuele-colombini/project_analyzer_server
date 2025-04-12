from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from architecture.arch_service import arch_service
from core.database_manager import database_manager

router = APIRouter(
    prefix='/architecture'
)


async def get_db():
    """Dependency for database session"""
    async with database_manager.AsyncSessionFactory() as session:
        yield session


@router.post("/{br_id}")
async def create_architecture(br_id: str, db: AsyncSession = Depends(get_db)):

    return await arch_service.create_architecture_analysis(db, br_id)

