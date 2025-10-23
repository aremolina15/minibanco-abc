# Backend/main.py
import sys
import os

# Agregar el directorio actual al path para imports absolutos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI

# Ahora usar imports absolutos
import database
import models

# Importar routers
from routers.auth import router as auth_router
from routers.users import router as users_router
from routers.accounts import router as accounts_router
from routers.transactions import router as transactions_router

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API Minibanco")

# Incluir routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(accounts_router)
app.include_router(transactions_router)

@app.get("/")
def root():
    return {"message": "Bienvenido al API del Minibanco"}