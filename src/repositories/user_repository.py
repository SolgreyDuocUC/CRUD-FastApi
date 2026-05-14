from sqlalchemy.orm import Session
from models.user import UsuarioModel
from schemas.user import UsuarioCreate, UsuarioUpdate
from utils.hashing import Hasher


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(UsuarioModel).all()

    def get_by_id(self, user_id: int):
        return self.db.query(UsuarioModel).filter(UsuarioModel.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    def create(self, user: UsuarioCreate):
        existing_user = self.get_by_email(user.email)

        if existing_user:
            raise ValueError("El email ya está registrado")

        db_user = UsuarioModel(
            nombre=user.nombre,
            email=user.email,
            edad=user.edad,
            password=Hasher.get_password_hash(user.password)
        )

        try:
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except Exception as e:
            self.db.rollback()
            raise e

    def update(self, user_id: int, user_update: UsuarioUpdate):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        
        if "password" in update_data:
            update_data["password"] = Hasher.get_password_hash(update_data["password"])
            
        for key, value in update_data.items():
            setattr(db_user, key, value)
            
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False
        self.db.delete(db_user)
        self.db.commit()
        return True
