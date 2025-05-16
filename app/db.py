from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine
from app.Settings import Settings

db_url = Settings().db_url

engine = create_engine(db_url)


def setup_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
