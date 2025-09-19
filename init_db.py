from app.core.database import engine, Base
from app.models.user import User
from app.models.project import Project

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    init_db()
