from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class CharacterActor(Base):
    __tablename__ = "characters_actors"

    character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)
    person_id = Column(Integer, ForeignKey("persons.id"), primary_key=True)
