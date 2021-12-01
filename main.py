from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

host = "postgresdb"
port = "5432"
user = "demo_user"
password = "password123"
db = "demo"
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict

from sqlalchemy import Column, Integer, String  # type: ignore


class ItemDict(TypedDict):
    name: str


class Item(Base):
    """
    Defines the items model
    """

    __tablename__ = "store"

    name = Column(String, primary_key=True)

    def __init__(self, name: str, ):
        self.name = name

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

    @property
    def serialize(self) -> ItemDict:
        """
        Return item in serializeable format
        """
        return {"name": self.name}


from sqlalchemy.orm import Session  # type: ignore


def post_item(session: Session, store_name: str) -> Item:
    n = Item(name=store_name)
    session.add(n)
    session.commit()


def get_item_by_name(session: Session, name: str) -> Item:
    return session.query(Item).filter(Item.name == name).first()


from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(alias="store_name")

    class Config:
        allow_population_by_field_name = True


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


@itemrouter.post("/store/",
                 response_model=ItemBase,
                 tags=["Items"],
                 description="Create a new item")
def post_fs_item(item_data: ItemBase, session: Session = Depends(get_session)):
    try:
        post_item(session=session, store_name=item_data.name)
    except Exception:
        raise HTTPException(status_code=400, detail="Issue while saving to DB")

    return item_data.__dict__


@itemrouter.get("/store/",
                response_model=ItemBase,
                tags=["Items"],
                description="Get a new item")
def read_item(store_name: str, session: Session = Depends(get_session)):
    item = get_item_by_name(session=session, name=store_name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize


from fastapi import FastAPI

app = FastAPI()
app.include_router(itemrouter)

import os

if os.environ['LOG_LEVEL'] == 'debug':
    print(os.environ['MODE'])
