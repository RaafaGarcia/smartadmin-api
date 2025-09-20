from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.core.database import SessionLocal
from app.models.user import User
from app.models.project import Project
from app.core.security import get_password_hash

def seed_data():
    """Seed database with sample data (Render-optimized)"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_users = db.query(User).count()
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
                "full_name": "Rafael García",
                "hashed_password": get_password_hash("password123")
            },
            {
                "email": "ana.lopez@example.com",
                "username": "ana",
                "full_name": "Ana López",
                "hashed_password": get_password_hash("password123")
            },
            {
                "email": "carlos.ruiz@example.com",
                "username": "carlos",
                "full_name": "Carlos Ruiz",
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
                "description": "Sistema ERP especializado en contaduría gubernamental desarrollado en Guadalajara",
                "status": "active",
                "priority": "high",
                "owner_id": admin_user.id
            },
            {
                "name": "Dashboard Analytics",
                "description": "Panel de métricas y analytics en tiempo real con FastAPI + React",
                "status": "active",
                "priority": "medium",
                "owner_id": admin_user.id
            },
            {
                "name": "SmartAdmin Mobile",
                "description": "Aplicación móvil para gestión de tareas administrativas",
                "status": "completed",
                "priority": "low",
                "owner_id": admin_user.id
            },
            {
                "name": "API Gateway Microservice",
                "description": "Microservicio para gestión centralizada de APIs",
                "status": "paused",
                "priority": "medium",
                "owner_id": admin_user.id
            },
            {
                "name": "Tech Lead Portfolio",
                "description": "Proyecto showcase para demostrar habilidades de liderazgo técnico",
                "status": "active",
                "priority": "high",
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
        
        return True
        
    except IntegrityError as e:
        print(f"⚠️  Data already exists, skipping: {e}")
        db.rollback()
        return True
    except Exception as e:
        print(f"❌ Error seeding data: {e}")
        db.rollback()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = seed_data()
    if not success:
        import sys
        sys.exit(1)