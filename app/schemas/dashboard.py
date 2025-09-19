from pydantic import BaseModel
from typing import List, Dict, Any

class DashboardMetrics(BaseModel):
    total_users: int
    active_projects: int
    completed_projects: int
    monthly_revenue: float

class ChartData(BaseModel):
    labels: List[str]
    data: List[float]

class DashboardData(BaseModel):
    metrics: DashboardMetrics
    user_growth: ChartData
    project_status: Dict[str, int]
    recent_activities: List[Dict[str, Any]]
