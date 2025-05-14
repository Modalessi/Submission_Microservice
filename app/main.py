from fastapi import FastAPI
from .schemas import SubmitSolutionRequest, SubmitSolutionResponse
from .services.submit_solution import _submit_solution
from .db import SessionDep

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/echo/{message}")
def echo_this(message: int, q: int = None):
    return {"message": message, "query": q}


@app.post("/submissions")
def submit_solution(submission_request: SubmitSolutionRequest, db: SessionDep) -> SubmitSolutionResponse:
    return _submit_solution(submit_solution_request=submission_request, db=db)
