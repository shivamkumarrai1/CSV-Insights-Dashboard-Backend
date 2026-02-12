from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..llm import generate_insights

router = APIRouter()


@router.post("/generate")
async def generate_report(data: schemas.GenerateInsightsRequest):
    summary = await generate_insights(data.columns, data.rows)
    return {"summary": summary}


@router.post("/")
def save_report(report: schemas.ReportCreate, db: Session = Depends(get_db)):
    db_report = models.Report(
        filename=report.filename,
        summary=report.summary
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


@router.get("/")
def get_reports(limit: int = 5, db: Session = Depends(get_db)):
    reports = (
        db.query(models.Report)
        .order_by(models.Report.created_at.desc())
        .limit(limit)
        .all()
    )
    return reports
