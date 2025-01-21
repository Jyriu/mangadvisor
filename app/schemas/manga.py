from datetime import date
from typing import Optional
from pydantic import BaseModel

class MangaBase(BaseModel):
    title: str
    title_english: Optional[str] = None
    title_japanese: Optional[str] = None
    synopsis: Optional[str] = None
    image_medium: Optional[str] = None
    image_large: Optional[str] = None
    media_type: str
    volumes: Optional[int] = None
    chapters: Optional[int] = None
    status: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    score: Optional[float] = None
    rank: Optional[int] = None
    popularity: Optional[int] = None

class MangaCreate(MangaBase):
    mal_id: int

class MangaUpdate(MangaBase):
    pass

class MangaInDBBase(MangaBase):
    id: int
    mal_id: int

    class Config:
        from_attributes = True

class Manga(MangaInDBBase):
    """Schéma pour retourner un manga"""
    pass

class MangaInDB(MangaInDBBase):
    """Schéma pour un manga en DB avec des champs supplémentaires si nécessaire"""
    pass 