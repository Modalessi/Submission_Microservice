from fastapi import HTTPException
from sqlmodel import select
from app.models import User
from app.schemas import LoginUserRequest, LoginUserResponse
from app.db import SessionDep
from app.auth.jwt import verify_password, create_access_token
from datetime import timedelta


def _login_user(login_request: LoginUserRequest, db: SessionDep) -> LoginUserResponse:
    stmt = select(User).where(User.username == login_request.username)
    user = db.exec(stmt).one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(
        data={"sub": str(user.ID), "username": user.username}, expires_delta=timedelta(minutes=30)
    )

    return LoginUserResponse(token=access_token)
