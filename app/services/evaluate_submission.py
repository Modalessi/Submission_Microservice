import asyncio
import random
from datetime import datetime
from sqlmodel import Session
from app.models import Submission
from app.enums import SubmissionStatus, SubmissionResult


async def evaluate_submission(submission_id: str, db: Session):

    await asyncio.sleep(random.uniform(2, 5))

    submission = db.get(Submission, submission_id)
    if not submission:
        return

    submission.status = SubmissionStatus.IN_PROGRESS
    db.add(submission)
    db.commit()

    possible_results = list(SubmissionResult)
    result = random.choice(possible_results)

    submission.status = SubmissionStatus.COMPLETED
    submission.result = result
    submission.updated_at = datetime.now()

    submission.execution_time = random.randint(100, 2000)
    submission.memory_usage = random.randint(1000, 50000)

    db.add(submission)
    db.commit()
