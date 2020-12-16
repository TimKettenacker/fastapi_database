# pydantic uses the word "model" to describe a schema actually (for validation)

from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
    # orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    # this way, it is not necessary to access id via data['id'], but by attribute too, data.id


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True