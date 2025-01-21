from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr

# Schéma de base pour l'utilisateur
class UserBase(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr

# Schéma pour la création d'un utilisateur
class UserCreate(UserBase):
    password: constr(min_length=8)

# Schéma pour la mise à jour d'un utilisateur
class UserUpdate(BaseModel):
    username: Optional[constr(min_length=3, max_length=50)] = None
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8)] = None

# Schéma de base pour l'utilisateur en DB
class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Schéma pour retourner un utilisateur (sans mot de passe)
class User(UserInDBBase):
    pass

# Schéma complet avec le mot de passe hashé (pour la DB)
class UserInDB(UserInDBBase):
    hashed_password: str

# Schéma pour l'authentification
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schéma pour le token
class Token(BaseModel):
    access_token: str
    token_type: str

# Schéma pour les données du token
class TokenPayload(BaseModel):
    sub: int  # user_id
    exp: datetime 