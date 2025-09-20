from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.core.database import get_db
from app.models.user import User
from app.models.project import Project
from app.schemas.dashboard import DashboardData, DashboardMetrics, ChartData

router = APIRouter()

@router.get("/metrics", response_model=DashboardData)
async def get_dashboard_metrics(db: Session = Depends(get_db)):
    # SQLAlchemy 2.0 queries
    total_users_stmt = select(func.count(User.id))
    total_users = db.execute(total_users_stmt).scalar()
    
    active_projects_stmt = select(func.count(Project.id)).where(Project.status == "active")
    active_projects = db.execute(active_projects_stmt).scalar()
    
    completed_projects_stmt = select(func.count(Project.id)).where(Project.status == "completed")
    completed_projects = db.execute(completed_projects_stmt).scalar()
    
    # Metrics
    metrics = DashboardMetrics(
        total_users=total_users or 42,
        active_projects=active_projects or 15,
        completed_projects=completed_projects or 28,
        monthly_revenue=48750.50
    )
    
    # Mock chart data
    user_growth = ChartData(
        labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        data=[10, 15, 22, 28, 35, total_users or 42]
    )
    
    project_status = {
        "active": active_projects or 15,
        "completed": completed_projects or 28,
        "paused": 3
    }
    
    recent_activities = [
        {
            "id": 1,
            "user": "Rafael García",
            "action": "Created new project",
            "project": "ERP Module",
            "time": "2 hours ago"
        },
        {
            "id": 2,
            "user": "Ana López",
            "action": "Completed task",
            "project": "Dashboard UI",
            "time": "4 hours ago"
        },
        {
            "id": 3,
            "user": "Carlos Ruiz",
            "action": "Updated user profile",
            "project": "User Management",
            "time": "6 hours ago"
        }
    ]
    
    return DashboardData(
        metrics=metrics,
        user_growth=user_growth,
        project_status=project_status,
        recent_activities=recent_activities
    )