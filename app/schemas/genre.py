from pydantic import BaseModel

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    mal_id: int

class GenreUpdate(GenreBase):
    pass

class GenreInDBBase(GenreBase):
    id: int
    mal_id: int

    class Config:
        from_attributes = True

class Genre(GenreInDBBase):
    """Schéma pour retourner un genre"""
    pass

class GenreInDB(GenreInDBBase):
    """Schéma pour un genre en DB"""
    pass 