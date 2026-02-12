import httpx
from .config import OPENROUTER_API_KEY, OPENROUTER_MODEL


async def generate_insights(columns, rows):
    prompt = f"""
You are a senior data analyst.

You MUST ONLY use the data provided below.
Do NOT use prior knowledge.
Do NOT assume missing years or values.
If something is not present, say "Not available in dataset".

Analyze strictly from the given rows.

CSV DATA
========
Columns:
{columns}

Rows:
{rows[:20]}

Provide:
1) Key trends
2) Possible outliers
3) What should be checked next

Keep the answer factual and based only on the dataset.

"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=60,
        )

    res.raise_for_status()
    data = res.json()

    return data["choices"][0]["message"]["content"]
