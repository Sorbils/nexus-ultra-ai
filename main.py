import os
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE = Path(__file__).parent
app = FastAPI(title="NEXUS ULTRA AI", version="0.1.0")

app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return (BASE / "static" / "index.html").read_text(encoding="utf-8")

@app.get("/api/health")
def health():
    return {"ok": True, "app": "NEXUS ULTRA AI", "time": datetime.now(timezone.utc).isoformat()}

@app.get("/api/status")
def status():
    # Safe initial release: paper mode only. No exchange credentials or order route.
    return {
        "name": "NEXUS ULTRA AI",
        "mode": "PAPER",
        "live_trading_enabled": False,
        "exchange_connected": False,
        "scanner": "NOT_CONFIGURED",
        "risk_profile": "MEDIUM",
        "max_open_positions": int(os.getenv("MAX_OPEN_POSITIONS", "3")),
        "daily_loss_limit_pct": float(os.getenv("DAILY_LOSS_LIMIT_PCT", "1.5")),
        "message": "İlk sürüm: canlı emir gönderimi kapalı."
    }
