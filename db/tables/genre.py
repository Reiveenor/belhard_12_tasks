from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from ..base import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(String(20), primary_key=True)
    name = Column(String(20), nullable=False)

    genre_of_film = relationship("Film",
                                 secondary='films_genres',
                                 cascade="all, delete",
                                 passive_deletes=True)
