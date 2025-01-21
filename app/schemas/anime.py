from datetime import date
from typing import Optional
from pydantic import BaseModel

class AnimeBase(BaseModel):
    title: str
    title_english: Optional[str] = None
    title_japanese: Optional[str] = None
    synopsis: Optional[str] = None
    image_medium: Optional[str] = None
    image_large: Optional[str] = None
    media_type: str
    episodes: Optional[int] = None
    status: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    season: Optional[str] = None
    season_year: Optional[int] = None
    rating: Optional[str] = None
    score: Optional[float] = None
    rank: Optional[int] = None
    popularity: Optional[int] = None

class AnimeCreate(AnimeBase):
    mal_id: int

class AnimeUpdate(AnimeBase):
    pass

class AnimeInDBBase(AnimeBase):
    id: int
    mal_id: int

    class Config:
        from_attributes = True

class Anime(AnimeInDBBase):
    """Schéma pour retourner un anime"""
    pass

class AnimeInDB(AnimeInDBBase):
    """Schéma pour un anime en DB avec des champs supplémentaires si nécessaire"""
    pass 