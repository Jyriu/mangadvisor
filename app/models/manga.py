from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

# Table d'association manga-genres
manga_genres = Table(
    'manga_genres',
    Base.metadata,
    Column('manga_id', Integer, ForeignKey('mangas.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Manga(Base):
    __tablename__ = "mangas"

    id = Column(Integer, primary_key=True, index=True)
    mal_id = Column(Integer, unique=True, index=True)
    title = Column(String, index=True)
    title_english = Column(String)
    title_japanese = Column(String)
    synopsis = Column(String)
    
    # Images
    image_medium = Column(String)
    image_large = Column(String)
    
    # Metadata
    media_type = Column(String)  # manga, novel, manhwa, etc.
    volumes = Column(Integer)
    chapters = Column(Integer)
    status = Column(String)  # publishing, finished, etc.
    start_date = Column(Date)
    end_date = Column(Date)
    
    # Ratings
    score = Column(Float)
    rank = Column(Integer)
    popularity = Column(Integer)
    
    # Timestamps
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    genres = relationship("Genre", secondary=manga_genres, back_populates="mangas") 