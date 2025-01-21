from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
import enum

class WatchStatus(enum.Enum):
    WATCHING = "watching"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"
    PLAN_TO_WATCH = "plan_to_watch"

class ReadStatus(enum.Enum):
    READING = "reading"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"
    PLAN_TO_READ = "plan_to_read"

# Tables d'association user-anime et user-manga avec données supplémentaires
class UserAnimeList(Base):
    __tablename__ = "user_anime_list"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    anime_id = Column(Integer, ForeignKey("animes.id"), primary_key=True)
    status = Column(Enum(WatchStatus))
    score = Column(Float)
    progress = Column(Integer)  # épisode actuel
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="anime_list")
    anime = relationship("Anime")

class UserMangaList(Base):
    __tablename__ = "user_manga_list"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    manga_id = Column(Integer, ForeignKey("mangas.id"), primary_key=True)
    status = Column(Enum(ReadStatus))
    score = Column(Float)
    chapters_read = Column(Integer)
    volumes_read = Column(Integer)
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="manga_list")
    manga = relationship("Manga")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # Timestamps
    created_at = Column(Date, default=datetime.utcnow)
    updated_at = Column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    anime_list = relationship("UserAnimeList", back_populates="user")
    manga_list = relationship("UserMangaList", back_populates="user") 