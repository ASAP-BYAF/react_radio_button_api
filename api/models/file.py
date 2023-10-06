from sqlalchemy import Column, Integer, String

from api.db import Base

class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vol_num = Column(Integer, nullable=False)
    file_num = Column(Integer, nullable=False)
    file_name = Column(String, nullable=False)