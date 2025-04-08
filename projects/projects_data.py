from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from core.database_manager import Entity


class ProjectEntity(Entity):
    __tablename__ = "Projects"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    project_folder: Mapped[str] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    update_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now(), onupdate=func.now())
    enabled: Mapped[bool] = mapped_column(nullable=False, default=True)
    disabled_date: Mapped[Optional[datetime]] = mapped_column(nullable=True)


class ProjectModel(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    project_folder: str
    creation_date: datetime
    update_date: datetime
    enabled: bool = True
    disabled_date: Optional[datetime] = None


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectUpdate(BaseModel):
    name: str
    description: Optional[str] = None


def to_model(entity: ProjectEntity) -> ProjectModel:
    """Convert a ProjectEntity to a ProjectModel model"""
    return ProjectModel(
        id=entity.id,
        name=entity.name,
        description=entity.description,
        project_folder=entity.project_folder,
        creation_date=entity.creation_date,
        update_date=entity.update_date,
        enabled=entity.enabled,
        disabled_date=entity.disabled_date
    )


def to_entity(model: ProjectModel) -> ProjectEntity:
    """Convert a ProjectModel model to a ProjectEntity"""
    return ProjectEntity(
        id=model.id,
        name=model.name,
        description=model.description,
        project_folder=model.project_folder,
        creation_date=model.creation_date,
        update_date=model.update_date,
        enabled=model.enabled,
        disabled_date=model.disabled_date
    )
    