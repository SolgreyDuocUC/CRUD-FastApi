from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    edad: int = Field(..., gt=0, lt=120)


class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=8)


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    edad: Optional[int] = Field(None, gt=0, lt=120)
    password: Optional[str] = Field(None, min_length=8)


class UsuarioResponse(UsuarioBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
