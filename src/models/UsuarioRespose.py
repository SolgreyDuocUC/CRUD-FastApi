from pydantic import BaseModel, EmailStr


class UsuarioResponse(BaseModel):

    id: int
    nombre: str
    email: EmailStr
    edad: int

    class Config:
        from_attributes = True