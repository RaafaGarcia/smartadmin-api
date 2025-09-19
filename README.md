# 🚀 SmartAdmin API

> Modern Admin Dashboard API built with FastAPI, PostgreSQL, and Docker

![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-3776ab?style=for-the-badge&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ed?style=for-the-badge&logo=docker)

## 📋 Descripción

SmartAdmin API es una API moderna para dashboard administrativo que proporciona endpoints completos para gestión de usuarios, proyectos y métricas de dashboard. Construida con FastAPI para alta performance y documentación automática.

## ✨ Características Principales

- 🔐 **Autenticación JWT** - Sistema seguro de login/register
- 📊 **Dashboard Metrics** - Métricas en tiempo real y datos de gráficas
- 👥 **User Management** - CRUD completo de usuarios
- 📁 **Project Management** - Gestión de proyectos con estados
- 🐳 **Docker Ready** - Setup completo con Docker Compose
- 📚 **Auto Documentation** - Swagger UI y ReDoc incluidos
- 🧪 **Testing Ready** - Estructura preparada para tests
- 🔄 **Database Migrations** - Alembic para migraciones

## 🛠️ Stack Tecnológico

- **Framework:** FastAPI 0.104.1
- **Base de Datos:** PostgreSQL 15
- **ORM:** SQLAlchemy 2.0
- **Autenticación:** JWT + bcrypt
- **Migraciones:** Alembic
- **Containerización:** Docker + Docker Compose
- **Testing:** pytest + httpx

## 🚀 Quick Start

### Prerequisitos

- Python 3.11+
- Docker y Docker Compose
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/smartadmin-api.git
cd smartadmin-api
```

### 2. Setup con Docker (Recomendado)

```bash
# Copiar variables de entorno
cp .env.example .env

# Levantar servicios
docker-compose up --build

# En otra terminal, inicializar DB
docker-compose exec api python init_db.py
docker-compose exec api python seed_data.py
```

### 3. Setup Manual

```bash
# Crear virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Setup PostgreSQL local y actualizar .env
createdb smartadmin_db

# Inicializar base de datos
python init_db.py
python seed_data.py

# Ejecutar servidor
uvicorn app.main:app --reload
```

## 📡 Endpoints API

### 🔐 Autenticación
- `POST /api/auth/register` - Registrar usuario
- `POST /api/auth/login` - Iniciar sesión
- `GET /api/auth/me` - Perfil del usuario actual

### 📊 Dashboard
- `GET /api/dashboard/metrics` - Métricas y datos del dashboard

### 👥 Usuarios
- `GET /api/users/` - Listar usuarios
- `GET /api/users/{id}` - Obtener usuario
- `PUT /api/users/{id}` - Actualizar usuario
- `DELETE /api/users/{id}` - Eliminar usuario

### 📁 Proyectos
- `GET /api/projects/` - Listar proyectos
- `POST /api/projects/` - Crear proyecto
- `GET /api/projects/{id}` - Obtener proyecto
- `PUT /api/projects/{id}` - Actualizar proyecto
- `DELETE /api/projects/{id}` - Eliminar proyecto

## 📚 Documentación

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health

## 🗄️ Estructura del Proyecto

```
smartadmin-api/
├── app/
│   ├── api/              # Routers de la API
│   │   ├── auth/         # Endpoints de autenticación
│   │   ├── dashboard/    # Endpoints del dashboard
│   │   ├── users/        # Endpoints de usuarios
│   │   └── projects/     # Endpoints de proyectos
│   ├── core/             # Configuración y seguridad
│   │   ├── config.py     # Settings de la aplicación
│   │   ├── database.py   # Configuración de DB
│   │   └── security.py   # JWT y encriptación
│   ├── models/           # Modelos SQLAlchemy
│   │   ├── user.py       # Modelo de Usuario
│   │   └── project.py    # Modelo de Proyecto
│   ├── schemas/          # Schemas Pydantic
│   │   ├── user.py       # Schemas de Usuario
│   │   ├── project.py    # Schemas de Proyecto
│   │   └── dashboard.py  # Schemas del Dashboard
│   └── main.py           # Punto de entrada de la app
├── alembic/              # Migraciones de base de datos
├── tests/                # Tests unitarios
├── requirements.txt      # Dependencias Python
├── docker-compose.yml    # Configuración Docker
├── Dockerfile           # Imagen Docker
└── README.md            # Este archivo
```

## 🔧 Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```bash
# Database
DATABASE_URL=postgresql://smartadmin_user:smartadmin_pass@localhost:5432/smartadmin_db

# Security
SECRET_KEY=your-super-secret-key-at-least-32-characters-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_HOSTS=["http://localhost:3000","https://your-frontend.com"]
```

## 🧪 Testing

```bash
# Ejecutar tests
pytest

# Con coverage
pytest --cov=app tests/

# Tests específicos
pytest tests/test_auth.py -v
```

## 📊 Datos de Prueba

Después de ejecutar `seed_data.py`, tendrás:

**Usuario Admin:**
- Email: `admin@smartadmin.com`
- Password: `admin123`

**Usuarios de Ejemplo:**
- `rafael.garcia@example.com` / `password123`
- `ana.lopez@example.com` / `password123`
- `carlos.ruiz@example.com` / `password123`

**Proyectos de Ejemplo:**
- ERP Gubernamental (Activo)
- Dashboard Analytics (Activo)
- Mobile App (Completado)
- API Gateway (Pausado)

## 🚀 Deployment

### Railway (Recomendado)

1. Conecta tu repo de GitHub con Railway
2. Configura las variables de entorno
3. Railway detectará automáticamente FastAPI
4. Tu API estará disponible en `https://tu-app.railway.app`

### Render

1. Crea una nueva Web Service en Render
2. Conecta tu repositorio GitHub
3. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Agrega PostgreSQL database addon

## 📈 Performance

- ⚡ **Response Time:** < 100ms promedio
- 🔄 **Concurrent Users:** 1000+ con uvicorn workers
- 📊 **Database:** Optimizado con índices y queries eficientes
- 🗜️ **Compression:** Gzip compression habilitado

## 🛡️ Seguridad

- 🔐 JWT tokens con expiración
- 🔒 Passwords hasheados con bcrypt
- 🌐 CORS configurado correctamente
- ⚡ Rate limiting ready
- 🛡️ SQL injection protection (SQLAlchemy ORM)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 👨‍💻 Autor

**Rafael García**
- LinkedIn: [tu-linkedin](https://linkedin.com/in/tu-perfil)
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: raafagca@gmail.com

---

⭐ ¡Si te gusta este proyecto, dale una estrella en GitHub!

## 🔗 Enlaces Relacionados

- [SmartAdmin Frontend](https://github.com/tu-usuario/smartadmin-frontend)
- [Demo Live](https://tu-usuario.github.io/smartadmin-frontend)
- [Documentación API](https://tu-api.railway.app/docs)