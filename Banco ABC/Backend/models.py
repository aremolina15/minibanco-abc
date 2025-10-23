# Backend/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

# CAMBIO: Importación absoluta en lugar de relativa
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    nombre = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    es_administrador = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    cuentas = relationship("Cuenta", back_populates="usuario")

class Cuenta(Base):
    __tablename__ = "cuentas"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    saldo = Column(Float, default=0)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="cuentas")
    transacciones = relationship("Transaccion", back_populates="cuenta")

class Transaccion(Base):
    __tablename__ = "transacciones"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    valor = Column(Float)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"))
    fecha = Column(DateTime, default=datetime.utcnow)
    cuenta = relationship("Cuenta", back_populates="transacciones")