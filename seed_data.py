from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from app.models.project import Project
from app.core.security import get_password_hash

def seed_data():
    """Seed database with sample data"""
    db = SessionLocal()
    
    try:
        # Create admin user
        admin_user = User(
            email="admin@smartadmin.com",
            username="admin",
            full_name="Administrator",
            hashed_password=get_password_hash("admin123"),
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        
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
        
        # Create sample projects
        projects_data = [
            {
                "name": "ERP Gubernamental",
                "description": "Sistema ERP especializado en contaduría gubernamental",
                "status": "active",
                "priority": "high",
                "owner_id": admin_user.id
            },
            {
                "name": "Dashboard Analytics",
                "description": "Panel de métricas y analytics en tiempo real",
                "status": "active",
                "priority": "medium",
                "owner_id": admin_user.id
            },
            {
                "name": "Mobile App",
                "description": "Aplicación móvil para gestión de tareas",
                "status": "completed",
                "priority": "low",
                "owner_id": admin_user.id
            },
            {
                "name": "API Gateway",
                "description": "Microservicio para gestión de APIs",
                "status": "paused",
                "priority": "medium",
                "owner_id": admin_user.id
            }
        ]
        
        for project_data in projects_data:
            project = Project(**project_data)
            db.add(project)
        
        db.commit()
        print("✅ Sample data seeded successfully!")
        print("👤 Admin user: admin@smartadmin.com / admin123")
        
    except Exception as e:
        print(f"❌ Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
