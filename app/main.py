from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import health, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CSV Insights Dashboard API")

origins = [
    "https://csv-insights-dashboard-chi.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
