from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)
    completed = Column(Boolean, default=False)
