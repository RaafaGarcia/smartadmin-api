import os
import sys
from sqlalchemy import text
from app.core.database import engine, Base, SessionLocal
from app.models.user import User
from app.models.project import Project

def init_db():
    """Initialize database tables for Render deployment"""
    try:
        print("🗄️  Creating database tables...")
        
        # Test connection first
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        
        # Check if tables exist and have data
        db = SessionLocal()
        user_count = db.query(User).count()
        print(f"📊 Current users in database: {user_count}")
        db.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False

if __name__ == "__main__":
    success = init_db()
    if not success:
        sys.exit(1)
    print("🚀 Database initialization completed!")