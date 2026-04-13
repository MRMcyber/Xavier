from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import health
import json
import time
from pathlib import Path

app = FastAPI(
    title="Xavier API",
    description="Backend API for Xavier News Verification & Digest Platform",
    version="1.0.0"
)

# #region agent log
with open(Path(__file__).resolve().parents[2] / "debug-90665e.log", "a", encoding="utf-8") as _f:
    _f.write(json.dumps({"sessionId":"90665e","runId":"initial","hypothesisId":"H5","location":"server/app/main.py:13","message":"Backend app module initialized","data":{"corsOrigins":settings.cors_origins},"timestamp":int(time.time() * 1000)}) + "\n")
# #endregion

# CORS Configuration
origins = [origin.strip() for origin in settings.cors_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from .routers import health, auth
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(auth.router, prefix="/api", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Xavier Backend API is running"}
