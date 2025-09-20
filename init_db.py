import sys
from sqlalchemy import text
from app.core.database import engine, Base, SessionLocal

def init_db():
    """Initialize database tables for modern SQLAlchemy"""
    try:
        print("🗄️  Creating database tables...")
        
        # Test connection first
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
        
        # Create all tables (SQLAlchemy 2.0 style)
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        
        # Check if tables exist and have data
        with SessionLocal() as db:
            from sqlalchemy import select, func
            from app.models.user import User
            
            stmt = select(func.count(User.id))
            user_count = db.execute(stmt).scalar()
            print(f"📊 Current users in database: {user_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False

if __name__ == "__main__":
    success = init_db()
    if not success:
        sys.exit(1)
    print("🚀 Database initialization completed!")