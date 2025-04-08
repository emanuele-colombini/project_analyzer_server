from datetime import datetime
from typing import Optional

from sqlalchemy import func, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from core.database_manager import Entity


class BusinessRequestEntity(Entity):
    __tablename__ = "business_requests"

    id: Mapped[str] = mapped_column(primary_key=True)
    project_id: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[int] = mapped_column(nullable=False)
    content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    file_path: Mapped[Optional[str]] = mapped_column(nullable=True)
    creation_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class BusinessRequestModel(BaseModel):
    id: str
    project_id: str
    version: int
    content: Optional[str] = None
    file_path: Optional[str] = None
    creation_date: datetime
    is_active: bool


class BusinessRequestCreate(BaseModel):
    project_id: str
    content: Optional[str] = None


class BusinessRequestFileUpload(BaseModel):
    project_id: str


def to_model(entity: BusinessRequestEntity) -> BusinessRequestModel:
    """Convert a BusinessRequestEntity to a BusinessRequestModel"""
    return BusinessRequestModel(
        id=entity.id,
        project_id=entity.project_id,
        version=entity.version,
        content=entity.content,
        file_path=entity.file_path,
        creation_date=entity.creation_date,
        is_active=entity.is_active
    )


def to_entity(model: BusinessRequestModel) -> BusinessRequestEntity:
    """Convert a BusinessRequestModel to a BusinessRequestEntity"""
    return BusinessRequestEntity(
        id=model.id,
        project_id=model.project_id,
        version=model.version,
        content=model.content,
        file_path=model.file_path,
        creation_date=model.creation_date,
        is_active=model.is_active
    )
