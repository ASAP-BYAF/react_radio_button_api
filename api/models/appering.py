from sqlalchemy import Column, Integer, String, ForeignKey

from api.db import Base

class Appearing(Base):
    __tablename__ = "appearing"

    # file_id = Column(Integer, primary_key=True)
    # task_id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('file.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)
#     Appearing_detail_id = Column(Integer, ForeignKey('appearing_detail.id'), nullable=False)

# class AppearingDetail(Base):
#     __tablename__ = "appearing_detail"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     Appearing_detail = Column(String, nullable=False)

