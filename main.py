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



def get_item_by_name(session: Session, name: str) -> Item:
    return session.query(Item).filter(Item.name == name).first()



def get_items(session: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return session.query(Item).offset(skip).limit(limit).all()


def post_item(session: Session, name: str) -> Item:
    n=Item(name=name)
    session.add(n)
    session.commit()





from pydantic import BaseModel




class ItemBase(BaseModel):
    name: str
    


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


@itemrouter.get("/store/", response_model=List[ItemBase])
def read_items(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    items = get_items(session=session, skip=skip, limit=limit)
    return [i.serialize for i in items]


@itemrouter.get("/store/{name}", response_model=ItemBase)
def read_item(name: str, session: Session = Depends(get_session)):
    item = get_item_by_name(session=session, name=name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize


@itemrouter.post("/store/{name}", response_model=ItemBase)
def post_fs_item(name: str, session: Session = Depends(get_session)):
    psitem = post_item(session=session, name=name)



from fastapi import FastAPI

app = FastAPI()
app.include_router(itemrouter)


