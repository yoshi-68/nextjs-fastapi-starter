from sqlalchemy import Column, Integer, String

from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
