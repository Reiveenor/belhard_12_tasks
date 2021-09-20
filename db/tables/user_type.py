from sqlalchemy import Column, String

from ..base import Base


class UserType(Base):
    __tablename__ = "user_types"

    id = Column(String(20), primary_key=True)
    name = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<UserType id={self.id}, name={self.name}>"
