from db.database import Base
from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime

class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    generation_date = Column(Date)
    content = Column(String)
    user_id = Column(Integer)
    course_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    
    
    
    