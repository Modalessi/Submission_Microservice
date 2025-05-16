from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from app.models import User
from app.db import get_session
from app.auth.jwt import verify_token

# Modify OAuth2 scheme to exclude WebSocket routes
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login", auto_error=False)


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)) -> User:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = verify_token(token)
    stmt = select(User).where(User.ID == payload["sub"])
    user = db.exec(stmt).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


get_current_user_dep = Depends(get_current_user)
