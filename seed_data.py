from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.core.database import SessionLocal
from app.models.user import User
from app.models.project import Project
from app.core.security import get_password_hash

def seed_data():
    """Seed database with sample data (SQLAlchemy 2.0 style)"""
    
    try:
        with SessionLocal() as db:
            # Check if data already exists (SQLAlchemy 2.0 style)
            stmt = select(User)
            existing_users = len(db.execute(stmt).scalars().all())
            
            if existing_users > 0:
                print(f"⚠️  Database already has {existing_users} users. Skipping seed.")
                return True
            
            print("🌱 Seeding database with sample data...")
            
            # Create admin user
            admin_user = User(
                email="admin@smartadmin.com",
                username="admin",
                full_name="Administrator",
                hashed_password=get_password_hash("admin123"),
                is_admin=True
            )
            db.add(admin_user)
            db.flush()  # Get ID without committing
            
            # Create sample users
            users_data = [
                {
                    "email": "rafael.garcia@example.com",
                    "username": "rafael",
                    "full_name": "Rafael García - Tech Lead Guadalajara",
                    "hashed_password": get_password_hash("password123")
                },
                {
                    "email": "ana.lopez@example.com",
                    "username": "ana",
                    "full_name": "Ana López - Frontend Developer",
                    "hashed_password": get_password_hash("password123")
                },
                {
                    "email": "carlos.ruiz@example.com",
                    "username": "carlos",
                    "full_name": "Carlos Ruiz - Backend Developer",
                    "hashed_password": get_password_hash("password123")
                },
                {
                    "email": "maria.gonzalez@example.com",
                    "username": "maria",
                    "full_name": "María González - UX Designer",
                    "hashed_password": get_password_hash("password123")
                }
            ]
            
            for user_data in users_data:
                user = User(**user_data)
                db.add(user)
            
            db.commit()
            print("✅ Users created successfully!")
            
            # Create sample projects
            projects_data = [
                {
                    "name": "ERP Gubernamental",
                    "description": "Sistema ERP especializado en contaduría gubernamental desarrollado en Guadalajara con metodologías Agile",
                    "status": "active",
                    "priority": "high",
                    "owner_id": admin_user.id
                },
                {
                    "name": "SmartAdmin Dashboard",
                    "description": "Panel de métricas y analytics en tiempo real con FastAPI + React + PostgreSQL",
                    "status": "active",
                    "priority": "high",
                    "owner_id": admin_user.id
                },
                {
                    "name": "Mobile App Flutter",
                    "description": "Aplicación móvil para gestión de tareas administrativas con Flutter",
                    "status": "completed",
                    "priority": "medium",
                    "owner_id": admin_user.id
                },
                {
                    "name": "API Gateway Microservice",
                    "description": "Microservicio para gestión centralizada de APIs con Docker y CI/CD",
                    "status": "active",
                    "priority": "medium",
                    "owner_id": admin_user.id
                },
                {
                    "name": "Tech Lead Portfolio",
                    "description": "Proyecto showcase para demostrar habilidades de liderazgo técnico y stack moderno",
                    "status": "active",
                    "priority": "high",
                    "owner_id": admin_user.id
                },
                {
                    "name": "Legacy System Migration",
                    "description": "Migración de sistema legacy en VB.NET a arquitectura moderna con microservicios",
                    "status": "paused",
                    "priority": "low",
                    "owner_id": admin_user.id
                }
            ]
            
            for project_data in projects_data:
                project = Project(**project_data)
                db.add(project)
            
            db.commit()
            print("✅ Projects created successfully!")
            print(f"🎉 Sample data seeded successfully!")
            print("👤 Admin credentials: admin@smartadmin.com / admin123")
            print("🔗 API Docs: /docs")
            print("📊 Dashboard: /api/dashboard/metrics")
            
        return True
        
    except IntegrityError as e:
        print(f"⚠️  Data already exists, skipping: {e}")
        return True
    except Exception as e:
        print(f"❌ Error seeding data: {e}")
        return False

if __name__ == "__main__":
    success = seed_data()
    if not success:
        import sys
        sys.exit(1)
