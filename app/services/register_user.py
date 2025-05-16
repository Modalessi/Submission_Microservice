from app.schemas import RegisterUserRequest, RegisterUserResponse
from app.models import User
from app.db import SessionDep
from app.auth.jwt import get_password_hash
from fastapi import HTTPException
from sqlmodel import select


def _register_user(register_request: RegisterUserRequest, db: SessionDep) -> RegisterUserResponse:

    stmt = select(User).where(User.username == register_request.username)
    existing_user = db.exec(stmt).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    stmt = select(User).where(User.email == register_request.email)
    existing_email = db.exec(stmt).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(register_request.password)
    new_user = User(
        username=register_request.username,
        password=hashed_password,
        email=register_request.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RegisterUserResponse(
        user_id=str(new_user.ID),
        username=new_user.username,
        email=new_user.email,
    )
