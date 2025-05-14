import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field
from .enums import SubmissionStatus, SubmissionResult


class User(SQLModel, table=True):
    ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid5)
    username: str


class Problem(SQLModel, table=True):
    ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid5)
    title: str
    description: str
    difficulty: str
    time_limit: int
    memory_limit: int
    created_at: datetime
    updated_at: datetime


class Submission(SQLModel, table=True):
    ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid5)
    user_id: uuid.UUID = Field(foreign_key="user.ID")
    language: str
    source_code: str
    status: SubmissionStatus = Field(default=SubmissionStatus.PENDING)
    result: SubmissionResult | None
    execution_time: int | None
    memory_usage: int | None
