from datetime import datetime
from typing import List

from sqlalchemy import func, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from core.core_data import Entity
from pydantic import BaseModel, Field


class BusinessRequestEntity(Entity):
    __tablename__ = "business_requests"

    id: Mapped[str] = mapped_column(primary_key=True)
    project_id: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[int] = mapped_column(nullable=False)
    file_path: Mapped[str] = mapped_column(nullable=False)
    creation_date: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class BusinessRequestModel(BaseModel):
    id: str
    project_id: str
    version: int
    file_path: str
    creation_date: datetime
    is_active: bool


class BusinessRequestCreate(BaseModel):
    project_id: str


def to_model(entity: BusinessRequestEntity) -> BusinessRequestModel:
    """Convert a BusinessRequestEntity to a BusinessRequestModel"""
    return BusinessRequestModel(
        id=entity.id,
        project_id=entity.project_id,
        version=entity.version,
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
        file_path=model.file_path,
        creation_date=model.creation_date,
        is_active=model.is_active
    )


class BusinessRequestEvaluationQuestion(BaseModel):
    """Model representing a Business Request evaluation question."""
    id: str = Field(..., description="Question ID (progressively numbered)")
    area: str = Field(..., description="Question area (name of paragraph/section from original document)")
    question: str = Field(..., description="Question to ask the client (formulated clearly and concisely)")
    motivation: str = Field(..., description="Question motivation (explanation of why this point needs clarification)")


class BusinessRequestEvaluationResult(BaseModel):
    """Model representing the complete result of a Business Request evaluation."""
    questions: List[BusinessRequestEvaluationQuestion] = Field([], description="List of evaluation questions")


class BusinessRequestEvaluationAnswers(BaseModel):
    """Model representing a Business Request evaluation question."""
    id: str = Field(..., description="Question ID (progressively numbered)")
    area: str = Field(..., description="Question area (name of paragraph/section from original document)")
    question: str = Field(..., description="Question to ask the client (formulated clearly and concisely)")
    answer: str = Field(..., description="")


class BusinessRequestAnswersResult(BaseModel):
    """Model representing the complete result of a Business Request evaluation."""
    answers: List[BusinessRequestEvaluationAnswers] = Field([], description="List of evaluation questions")