from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

# Table d'association anime-genres
anime_genres = Table(
    'anime_genres',
    Base.metadata,
    Column('anime_id', Integer, ForeignKey('animes.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

# Table d'association anime-studios
anime_studios = Table(
    'anime_studios',
    Base.metadata,
    Column('anime_id', Integer, ForeignKey('animes.id'), primary_key=True),
    Column('studio_id', Integer, ForeignKey('studios.id'), primary_key=True)
)

class Anime(Base):
    __tablename__ = "animes"

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
    media_type = Column(String)  # tv, movie, ova, etc.
    episodes = Column(Integer)
    status = Column(String)  # airing, finished_airing, etc.
    start_date = Column(Date)
    end_date = Column(Date)
    season = Column(String)  # spring, summer, fall, winter
    season_year = Column(Integer)
    
    # Ratings
    rating = Column(String)  # pg_13, r, etc.
    score = Column(Float)
    rank = Column(Integer)
    popularity = Column(Integer)
    
    # Timestamps
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    genres = relationship("Genre", secondary=anime_genres, back_populates="animes")
    studios = relationship("Studio", secondary=anime_studios, back_populates="animes") 