from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

class UserService:
    def get(self, db: Session, user_id: int) -> Optional[User]:
        """Récupère un utilisateur par son ID."""
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Récupère un utilisateur par son email."""
        return db.query(User).filter(User.email == email).first()

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        """Récupère un utilisateur par son username."""
        return db.query(User).filter(User.username == username).first()

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        """Authentifie un utilisateur avec email/password."""
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def create(self, db: Session, user_in: UserCreate) -> User:
        """Crée un nouvel utilisateur."""
        db_user = User(
            email=user_in.email,
            username=user_in.username,
            hashed_password=get_password_hash(user_in.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, user: User, user_in: UserUpdate) -> User:
        """Met à jour un utilisateur."""
        update_data = user_in.model_dump(exclude_unset=True)
        
        if "password" in update_data:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        for field, value in update_data.items():
            setattr(user, field, value)

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user_id: int) -> Optional[User]:
        """Supprime un utilisateur."""
        user = self.get(db, user_id)
        if user:
            db.delete(user)
            db.commit()
        return user


# Création d'une instance unique du service
user_service = UserService() 