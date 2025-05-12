from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze_risk")
def analyze_risk(allocation_today: float, allocation_yesterday: float):
    change = allocation_today - allocation_yesterday
    risk_level = "High" if change > 5 else "Moderate" if change > 0 else "Stable"
    return {"risk_change": change, "risk_level": risk_level}