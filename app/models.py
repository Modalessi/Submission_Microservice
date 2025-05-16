import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field
from .enums import SubmissionStatus, SubmissionResult


class User(SQLModel, table=True):
    __tablename__ = "users"
    ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    username: str
    password: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Submission(SQLModel, table=True):
    __tablename__ = "submissions"
    ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    user_id: uuid.UUID = Field(foreign_key="users.ID")
    problem_id: uuid.UUID
    language: str
    source_code: str
    status: SubmissionStatus = Field(default=SubmissionStatus.PENDING)
    result: SubmissionResult | None
    execution_time: int | None
    memory_usage: int | None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
