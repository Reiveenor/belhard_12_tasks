from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from ..base import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, autoincrement=True)
    duration = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    release_date = Column(DateTime, nullable=False)
    rating = Column(Float(3, 2), nullable=False)
    director_id = Column(Integer, ForeignKey("persons.id"), nullable=False)

    director = relationship("Person")

    users_liked = relationship("User",
                               secondary="user_favorite_films",
                               cascade="all, delete",
                               passive_deletes=True)
    film_genre = relationship("Genre",
                              secondary="films_genres",
                              cascade="all, delete",
                              passive_deletes=True)
