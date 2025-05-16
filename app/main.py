from typing import List
from fastapi import FastAPI, BackgroundTasks
from .schemas import SubmitSolutionRequest, SubmitSolutionResponse, GetSubmissionResponse
from .schemas import RegisterUserRequest, RegisterUserResponse
from .schemas import LoginUserRequest, LoginUserResponse
from .services.submit_solution import _submit_solution
from .services.register_user import _register_user
from .services.login_user import _login_user
from .services.get_submission import _get_submission
from .services.get_user_submissions import _get_user_submissions

from .db import SessionDep
from .auth.deps import get_current_user_dep
from .models import User
from .rate_limiter import rate_limit_dep

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/users/register")
def register_user(register_request: RegisterUserRequest, db: SessionDep) -> RegisterUserResponse:
    return _register_user(register_request=register_request, db=db)


@app.post("/users/login")
def login_user(login_request: LoginUserRequest, db: SessionDep) -> LoginUserResponse:
    return _login_user(login_request=login_request, db=db)


@app.post("/submissions", dependencies=[rate_limit_dep])
def submit_solution(
    submission_request: SubmitSolutionRequest,
    background_tasks: BackgroundTasks,
    db: SessionDep,
    current_user: User = get_current_user_dep,
) -> SubmitSolutionResponse:
    return _submit_solution(
        submit_solution_request=submission_request,
        db=db,
        current_user=current_user,
        background_tasks=background_tasks,
    )


@app.get("/submissions/{submission_id}")
def get_submission(submission_id: str, db: SessionDep) -> GetSubmissionResponse:
    return _get_submission(submission_id=submission_id, db=db)


@app.get("/users/{user_id}/submissions")
def get_user_submissions(user_id: str, db: SessionDep) -> List[GetSubmissionResponse]:
    return _get_user_submissions(user_id=user_id, db=db)
