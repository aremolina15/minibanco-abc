from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ESQUEMAS EXISTENTES (modificados)
class UsuarioBase(BaseModel):
    identificacion: str
    nombre: str
    email: str  # CAMBIO: usar str en lugar de EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    es_administrador: Optional[bool] = False

class Usuario(UsuarioBase):
    id: int
    es_administrador: bool
    activo: bool
    fecha_creacion: datetime
    class Config:
        orm_mode = True

# NUEVOS ESQUEMAS PARA AUTENTICACIÓN
class UserLogin(BaseModel):
    email: str  # CAMBIO: usar str en lugar de EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: Usuario

class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[int] = None

# Esquemas existentes (sin cambios)
class CuentaBase(BaseModel):
    tipo: str

class CuentaCreate(CuentaBase):
    usuario_id: int

class Cuenta(CuentaBase):
    id: int
    saldo: float
    usuario_id: int
    class Config:
        orm_mode = True

class TransaccionBase(BaseModel):
    tipo: str
    valor: float

class TransaccionCreate(TransaccionBase):
    cuenta_id: int

class Transaccion(TransaccionBase):
    id: int
    cuenta_id: int
    fecha: datetime
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: Usuario  # Este campo debe llamarse 'user'