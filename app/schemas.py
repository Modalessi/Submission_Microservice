from pydantic import BaseModel
from .enums import SubmissionStatus


class SubmitSolutionRequest(BaseModel):
    user_id: str
    problem_id: str
    language: str
    source_code: str


class SubmitSolutionResponse(BaseModel):
    submission_id: str
    status: SubmissionStatus = SubmissionStatus.PENDING
