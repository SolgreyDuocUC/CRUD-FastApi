from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.user import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from repositories.user_repository import UserRepository

router = APIRouter(
    prefix="/api/v1/usuarios",
    tags=["usuarios"]
)


@router.get("/", response_model=List[UsuarioResponse])
def read_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all()


@router.get("/{user_id}", response_model=UsuarioResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    db_user = repo.get_by_id(user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return db_user


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UsuarioCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    db_user = repo.get_by_email(user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )
    return repo.create(user)


@router.put("/{user_id}", response_model=UsuarioResponse)
def update_user(user_id: int, user: UsuarioUpdate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    updated_user = repo.update(user_id, user)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    success = repo.delete(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return None
