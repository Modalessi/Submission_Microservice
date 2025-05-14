from app.schemas import SubmitSolutionRequest, SubmitSolutionResponse
from app.models import Submission
from app.db import SessionDep


def _submit_solution(submit_solution_request: SubmitSolutionRequest, db: SessionDep) -> SubmitSolutionResponse:
    new_submission = Submission(
        user_id="current_user_id",
        problem_id="current_problem_id",
        language=submit_solution_request.language,
        source_code=submit_solution_request.source_code,
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return SubmitSolutionResponse(
        submission_id=str(new_submission.ID),
        status=new_submission.status,
    )
