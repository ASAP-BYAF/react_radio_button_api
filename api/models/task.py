from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), unique=True)
    # appearing = relationship("Appearing", cascade="delete")
    # projects = relationship("File",
    #                         back_populates="file")
