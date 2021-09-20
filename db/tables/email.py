from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    user_login = Column(String(20), ForeignKey("users.login"), nullable=False)

    user = relationship("User")
