# the "base" class created in "database.py" is used as a baseline to create the models out of it

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# this class is a SQLAlchemy model, ORM represents a table in the database
# attributes represent a column in the database table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")
    # "relationship" contains the values from other tables related to this one, so if user items are
    # accessed, SQLAlchemy will actually go and fetch the items from the database in the items table
    # using the owner attribute (foreign key) in the items table

# this class is another SQLAlchemy model, it represents another table in the database
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")