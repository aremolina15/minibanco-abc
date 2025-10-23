# Backend/reset_db.py
import os
import sys

# Agregar el directorio actual al path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Importaciones después de agregar al path
from database import engine
from models import Base

print("🗑️  Eliminando tablas existentes...")
Base.metadata.drop_all(bind=engine)

print("🔄 Creando nuevas tablas...")
Base.metadata.create_all(bind=engine)

print("✅ Base de datos recreada exitosamente!")