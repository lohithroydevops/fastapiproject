import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

host = "postgresdb"
port =  "5432"
user = "demo_user"
password = "password123"
db = "demo"
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Literal, overload  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict, Literal, overload


from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.orm import relationship


class ItemDict(TypedDict):
    name: str


class Item(Base):
    """
    Defines the items model
    """

    __tablename__ = "store"

    name = Column(String, primary_key=True)

    def __init__(self,  name: str, ):
        self.name = name

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

    @property
    def serialize(self) -> ItemDict:
        """
        Return item in serializeable format
        """
        return {"name": self.name}

from typing import List
from sqlalchemy.orm import Session  # type: ignore
def post_item(session: Session, store_name: str) -> Item:
    n=Item(name=store_name)
    session.add(n)
    session.commit()

from pydantic import BaseModel, Field
class ItemBase(BaseModel):
    name: str = Field(alias="store_name")

    class Config:
        allow_population_by_field_name = True
    
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore

Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@itemrouter.post("/store/", response_model=ItemBase)
def post_fs_item(store_name: str, session: Session = Depends(get_session)):
    psitem = post_item(session=session, store_name=store_name)

from fastapi import FastAPI

app = FastAPI()
app.include_router(itemrouter)

import os

if(os.environ['LOG_LEVEL'] == 'debug'):
    print(os.environ['MODE'])
