from pydantic import BaseModel
from .enums import SubmissionStatus, SubmissionResult
import uuid


class SubmitSolutionRequest(BaseModel):
    user_id: uuid.UUID
    problem_id: uuid.UUID
    language: str
    source_code: str


class SubmitSolutionResponse(BaseModel):
    submission_id: str
    status: SubmissionStatus = SubmissionStatus.PENDING


class GetSubmissionResponse(BaseModel):

    user_id: uuid.UUID
    problem_id: uuid.UUID
    language: str
    source_code: str
    status: SubmissionStatus
    result: SubmissionResult | None
    execution_time: int | None


class RegisterUserRequest(BaseModel):
    username: str
    password: str
    email: str


class RegisterUserResponse(BaseModel):
    user_id: str
    username: str
    email: str


class LoginUserRequest(BaseModel):
    username: str
    password: str


class LoginUserResponse(BaseModel):
    token: str
