from app.models import Submission
from app.db import SessionDep
from app.schemas import GetSubmissionResponse
from sqlmodel import select
from typing import List


def _get_user_submissions(user_id: str, db: SessionDep) -> List[GetSubmissionResponse]:
    stmt = select(Submission).where(Submission.user_id == user_id)
    submissions = db.exec(stmt).all()
    return [
        GetSubmissionResponse(
            user_id=submission.user_id,
            problem_id=submission.problem_id,
            language=submission.language,
            source_code=submission.source_code,
            status=submission.status,
            result=submission.result,
            execution_time=submission.execution_time,
            memory_usage=submission.memory_usage,
        )
        for submission in submissions
    ]
