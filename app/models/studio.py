from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Studio(Base):
    __tablename__ = "studios"

    id = Column(Integer, primary_key=True, index=True)
    mal_id = Column(Integer, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Relations
    animes = relationship("Anime", secondary="anime_studios", back_populates="studios") 