# Backend/test_db_write.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal, engine
from models import Base, Usuario
from security import get_password_hash

print("🧪 Probando escritura en la base de datos...")

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    # Intentar insertar un usuario de prueba
    test_user = Usuario(
        identificacion="test_write_001",
        nombre="Test Escritura",
        email="test@write.com", 
        password_hash=get_password_hash("test123"),
        es_administrador=False
    )
    
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    
    print("✅ ✅ ✅ ESCRITURA EXITOSA en la base de datos")
    print(f"Usuario insertado: {test_user.nombre} (ID: {test_user.id})")
    
except Exception as e:
    print(f"❌ ❌ ❌ ERROR en escritura: {e}")
finally:
    db.close()