# Backend/recreate_db.py
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# CAMBIO: Importaciones absolutas
from database import engine
from models import Base

print("🗑️  Eliminando tablas existentes...")
Base.metadata.drop_all(bind=engine)

print("🔄 Creando nuevas tablas...")
Base.metadata.create_all(bind=engine)

print("✅ Base de datos recreada con los nuevos campos")