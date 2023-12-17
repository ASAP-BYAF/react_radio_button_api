from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.db import Base


class Appearing(Base):
    __tablename__ = "appearing"

    file_id = Column(Integer, ForeignKey('file.id', ondelete="CASCADE"), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete="CASCADE"), primary_key=True)
    appearing_detail_id = Column(Integer,
                                 ForeignKey('appearing_detail.id',
                                            ondelete="CASCADE"),
                                 nullable=False)
class AppearingDetail(Base):
    __tablename__ = "appearing_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    appearing_detail = Column(String, nullable=False, unique=True)
