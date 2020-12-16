# is taken from https://fastapi.tiangolo.com/tutorial/sql-databases/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# sqlite is in fact just a file mimicking a lightweight version of a RDBMS, for example its single-thread

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# instances of this class will actually be database sessions

Base = declarative_base()