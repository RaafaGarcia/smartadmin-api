from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.core.config import settings
from app.api.auth.router import router as auth_router
from app.api.dashboard.router import router as dashboard_router
from app.api.users.router import router as users_router
from app.api.projects.router import router as projects_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if os.getenv("RENDER"):
        print("🌐 Running on Render - initializing database...")
        try:
            from init_db import init_db
            from seed_data import seed_data
            
            init_success = init_db()
            if init_success:
                seed_data()
        except Exception as e:
            print(f"⚠️  Database initialization error: {e}")
    yield
    # Shutdown
    print("👋 Shutting down SmartAdmin API...")

app = FastAPI(
    title="SmartAdmin API",
    description="Modern Admin Dashboard API built with FastAPI 0.104 + SQLAlchemy 2.0 - Deployed on Render",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(dashboard_router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(projects_router, prefix="/api/projects", tags=["Projects"])

@app.get("/")
async def root():
    return {
        "message": "SmartAdmin API v2.0.0 - Modern Stack",
        "stack": "FastAPI 0.104 + SQLAlchemy 2.0 + Pydantic Settings",
        "docs": "/docs",
        "status": "running",
        "author": "Rafael García - Tech Lead Guadalajara"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "version": "2.0.0",
        "stack": "modern",
        "database": "postgresql"
    }