from fastapi import APIRouter
from sqlalchemy import text
import httpx
from ..database import engine
from ..config import OPENROUTER_API_KEY

router = APIRouter()


@router.get("/")
async def health():
    # backend OK if route runs
    backend = "ok"

    # DB check
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        database = "ok"
    except Exception:
        database = "error"

    # LLM check
    try:
        headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
        async with httpx.AsyncClient() as client:
            r = await client.get("https://openrouter.ai/api/v1/models", headers=headers)
        llm = "ok" if r.status_code == 200 else "error"
    except Exception:
        llm = "error"

    return {
        "backend": backend,
        "database": database,
        "llm": llm,
    }
