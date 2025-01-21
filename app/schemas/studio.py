from pydantic import BaseModel

class StudioBase(BaseModel):
    name: str

class StudioCreate(StudioBase):
    mal_id: int

class StudioUpdate(StudioBase):
    pass

class StudioInDBBase(StudioBase):
    id: int
    mal_id: int

    class Config:
        from_attributes = True

class Studio(StudioInDBBase):
    """Schéma pour retourner un studio"""
    pass

class StudioInDB(StudioInDBBase):
    """Schéma pour un studio en DB"""
    pass 