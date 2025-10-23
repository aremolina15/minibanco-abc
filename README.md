# 🏦 Minibanco ABC

Sistema bancario completo con backend en FastAPI y frontend en Django.

## 📁 Estructura del Proyecto

```
BANCO ABC/
├── Backend/                 # API FastAPI
│   ├── routers/            # Endpoints de la API
│   ├── models.py           # Modelos de base de datos
│   ├── database.py         # Configuración de BD
│   ├── schemas.py          # Esquemas Pydantic
│   └── main.py             # Aplicación principal
├── frontend_django/        # Frontend Django
│   ├── banco/              # App principal Django
│   ├── frontend_django/    # Configuración Django
│   ├── manage.py
│   └── db.sqlite3
└── README.md
```

## 🚀 Características

### Backend (FastAPI)
- ✅ API RESTful completa
- ✅ Documentación automática (Swagger/OpenAPI)
- ✅ Base de datos SQLite
- ✅ Modelos: Usuarios, Cuentas, Transacciones
- ✅ Autenticación (si está implementada)

### Frontend (Django)
- ✅ Interfaz web administrativa
- ✅ Gestión de clientes y cuentas
- ✅ Panel de transacciones
- ✅ Base de datos SQLite

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)

### 1. Clonar o descargar el proyecto
```bash
cd "Documents/Eje1 Desarrollo Web/Banco ABC"
```

### 2. Configurar Backend (FastAPI)

```bash
# Navegar al directorio del backend
cd Backend

# Crear entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install fastapi uvicorn sqlalchemy python-multipart

# Ejecutar el servidor
uvicorn main:app --reload --port 8001
```

El backend estará disponible en: http://127.0.0.1:8001

### 3. Configurar Frontend (Django)

```bash
# En una nueva terminal, navegar al frontend
cd frontend_django

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Instalar dependencias
pip install django requests

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver 8000
```

El frontend estará disponible en: http://127.0.0.1:8000

## 📚 Documentación de la API

Una vez ejecutado el backend, accede a:
- **Swagger UI**: http://127.0.0.1:8001/docs
- **ReDoc**: http://127.0.0.1:8001/redoc

## 🔌 Endpoints Principales

### Usuarios
- `GET /users/` - Listar usuarios
- `POST /users/` - Crear usuario
- `GET /users/{id}` - Obtener usuario específico

### Cuentas
- `GET /accounts/` - Listar cuentas
- `POST /accounts/` - Crear cuenta
- `GET /accounts/{id}` - Obtener cuenta específica

### Transacciones
- `GET /transactions/` - Listar transacciones
- `POST /transactions/` - Crear transacción
- `GET /transactions/{id}` - Obtener transacción específica

## 🗄️ Modelos de Datos

### Usuario
- id: int
- nombre: str
- email: str
- fecha_creacion: datetime

### Cuenta
- id: int
- usuario_id: int
- saldo: float
- tipo_cuenta: str
- fecha_apertura: datetime

### Transacción
- id: int
- cuenta_id: int
- monto: float
- tipo: str (deposito/retiro)
- fecha: datetime

## 👨‍💻 Uso del Sistema

### Como Administrador
1. Accede al panel de Django: http://127.0.0.1:8000/admin
2. Gestiona usuarios, cuentas y transacciones
3. Visualiza reportes y estadísticas

### Como Cliente (API)
1. Consulta tu información: `GET /users/{tu_id}`
2. Revisa tu cuenta: `GET /accounts/?usuario_id={tu_id}`
3. Realiza transacciones: `POST /transactions/`

## 🐛 Solución de Problemas

### Error: Puerto en uso
```bash
# Encontrar proceso
sudo netstat -tulpn | grep :8000

# Matar proceso
sudo kill -9 <PID>

# O usar puerto diferente
uvicorn main:app --reload --port 8002
```

### Error: Importación de módulos
- Verificar que todos los archivos `__init__.py` existan
- Ejecutar desde el directorio correcto
- Usar importaciones absolutas en lugar de relativas

### Error: Base de datos
```bash
# En Django
python manage.py makemigrations
python manage.py migrate

# En FastAPI, verificar que database.py esté configurado correctamente
```

## 📝 Notas de Desarrollo

- El backend usa SQLAlchemy para ORM
- El frontend usa el ORM nativo de Django
- La comunicación entre frontend y backend se realiza via API REST
- Base de datos SQLite para desarrollo (fácil de migrar a PostgreSQL en producción)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es para fines educativos.

## 👥 Autor

Desarrollado por: Anghie Remolina.

---

**¿Necesitas ayuda?** Revisa la documentación en `/docs` o abre un issue en el repositorio.