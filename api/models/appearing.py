from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
from api.db import Base


class Appearing(Base):
    __tablename__ = "appearing"

    # file_id = Column(Integer, primary_key=True)
    # task_id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('file.id'), primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)
    appearing_detail_id = Column(Integer,
                                 ForeignKey('appearing_detail.id'),
                                 nullable=False)
    # user = relationship("User", back_populates="projects")
    # project = relationship("Project", back_populates="users")
    # # proxies
    # user_name = association_proxy(target_collection="user", attr="name")
    # project_name = association_proxy(target_collection="project", attr="name")


class AppearingDetail(Base):
    __tablename__ = "appearing_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    appearing_detail = Column(String, nullable=False, unique=True)
