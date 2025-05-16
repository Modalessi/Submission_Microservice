from app.schemas import SubmitSolutionRequest, SubmitSolutionResponse
from app.models import Submission, User
from app.services.evaluate_submission import evaluate_submission
from app.db import SessionDep
from fastapi import BackgroundTasks, HTTPException


def _submit_solution(
    submit_solution_request: SubmitSolutionRequest,
    db: SessionDep,
    current_user: User,
    background_tasks: BackgroundTasks,
) -> SubmitSolutionResponse:
    if str(current_user.ID) != str(submit_solution_request.user_id):
        raise HTTPException(status_code=403, detail="Not authorized to submit for this user")

    new_submission = Submission(
        user_id=submit_solution_request.user_id,
        language=submit_solution_request.language,
        source_code=submit_solution_request.source_code,
        problem_id=submit_solution_request.problem_id,
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    background_tasks.add_task(
        evaluate_submission,
        submission_id=str(new_submission.ID),
        db=db,
    )

    return SubmitSolutionResponse(
        submission_id=str(new_submission.ID),
        status=new_submission.status,
    )
