from fastapi import FastAPI
from typing import Any, Dict
import json
from datetime import datetime
from pathlib import Path

app = FastAPI(title="main")

EXAMPLES_DIR = Path("examples")
EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/webhook")
async def hi(data: Dict[str, Any]):
    ts = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    file_path = EXAMPLES_DIR / f"entrada_{ts}.json"
    file_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"msg": "main", "saved": str(file_path)}
 