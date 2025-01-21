from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

# Enums pour les statuts
class WatchStatus(str, Enum):
    WATCHING = "watching"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"
    PLAN_TO_WATCH = "plan_to_watch"

class ReadStatus(str, Enum):
    READING = "reading"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"
    PLAN_TO_READ = "plan_to_read"

# Schémas pour la liste d'animes
class UserAnimeListBase(BaseModel):
    anime_id: int
    status: WatchStatus
    score: Optional[float] = Field(None, ge=0, le=10)
    progress: Optional[int] = Field(None, ge=0)

class UserAnimeListCreate(UserAnimeListBase):
    pass

class UserAnimeListUpdate(BaseModel):
    status: Optional[WatchStatus] = None
    score: Optional[float] = Field(None, ge=0, le=10)
    progress: Optional[int] = Field(None, ge=0)

class UserAnimeListInDB(UserAnimeListBase):
    user_id: int
    updated_at: datetime

    class Config:
        from_attributes = True

# Schémas pour la liste de mangas
class UserMangaListBase(BaseModel):
    manga_id: int
    status: ReadStatus
    score: Optional[float] = Field(None, ge=0, le=10)
    chapters_read: Optional[int] = Field(None, ge=0)
    volumes_read: Optional[int] = Field(None, ge=0)

class UserMangaListCreate(UserMangaListBase):
    pass

class UserMangaListUpdate(BaseModel):
    status: Optional[ReadStatus] = None
    score: Optional[float] = Field(None, ge=0, le=10)
    chapters_read: Optional[int] = Field(None, ge=0)
    volumes_read: Optional[int] = Field(None, ge=0)

class UserMangaListInDB(UserMangaListBase):
    user_id: int
    updated_at: datetime

    class Config:
        from_attributes = True 