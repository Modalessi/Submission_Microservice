from app.models import Submission
from app.db import SessionDep
from app.schemas import GetSubmissionResponse
from sqlmodel import select
from fastapi import HTTPException


def _get_submission(submission_id: str, db: SessionDep) -> GetSubmissionResponse:
    stmt = select(Submission).where(Submission.ID == submission_id)
    submission = db.exec(stmt).one_or_none()

    if submission is None:
        raise HTTPException(status_code=404, detail="Submission not found")

    return GetSubmissionResponse(
        user_id=submission.user_id,
        problem_id=submission.problem_id,
        language=submission.language,
        source_code=submission.source_code,
        status=submission.status,
        result=submission.result,
        execution_time=submission.execution_time,
        memory_usage=submission.memory_usage,
    )
