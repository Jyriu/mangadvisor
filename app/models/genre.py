from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    mal_id = Column(Integer, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Relations
    animes = relationship("Anime", secondary="anime_genres", back_populates="genres")
    mangas = relationship("Manga", secondary="manga_genres", back_populates="genres") 