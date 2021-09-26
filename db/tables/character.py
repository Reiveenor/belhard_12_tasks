from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    comment = Column(String(100))
    film_id = Column(Integer, ForeignKey("films.id"), nullable=False)

    char_of_film = relationship("Film")

    char_person = relationship("Person",
                               secondary="characters_actors",
                               cascade="all, delete",
                               passive_deletes=True)
