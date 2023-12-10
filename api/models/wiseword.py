from sqlalchemy import Column, Integer, String, ForeignKey
from api.db import Base


class Wiseword(Base):
    __tablename__ = "wiseword"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phrase = Column(String, nullable=False, unique=True)
    file_id = Column(Integer, ForeignKey('file.id'))
