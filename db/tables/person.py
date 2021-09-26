from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..base import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    birth_date = Column(DateTime, nullable=False)

    person_char = relationship("Character",
                               secondary="characters_actors",
                               cascade="all, delete",
                               passive_deletes=True)
