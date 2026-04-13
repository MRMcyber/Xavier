from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from pydantic import BaseModel
from ..config import settings
import json
import time
from pathlib import Path

router = APIRouter(prefix="/auth", tags=["Authentication"])

security = HTTPBearer()

def get_supabase() -> Client:
    # #region agent log
    with open(Path(__file__).resolve().parents[3] / "debug-90665e.log", "a", encoding="utf-8") as _f:
        _f.write(json.dumps({"sessionId":"90665e","runId":"initial","hypothesisId":"H4","location":"server/app/routers/auth.py:14","message":"Creating backend Supabase client","data":{"urlPreview":settings.supabase_url[:40],"urlLooksPlaceholder":"your-project.supabase.co" in settings.supabase_url,"hasServiceRole":bool(settings.supabase_service_role_key),"serviceRoleLooksPlaceholder":settings.supabase_service_role_key == "your-service-role-key-here"},"timestamp":int(time.time() * 1000)}) + "\n")
    # #endregion
    return create_client(settings.supabase_url, settings.supabase_service_role_key or settings.supabase_anon_key)

async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Verify the Supabase JWT token received from the frontend.
    """
    token = credentials.credentials
    supabase = get_supabase()
    try:
        # Supabase auth.get_user(token) verifies the token against the Supabase server
        user_res = supabase.auth.get_user(token)
        if not user_res.user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_res.user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

class UserProfile(BaseModel):
    id: str
    email: str

@router.get("/me", response_model=UserProfile)
async def get_current_user(user = Depends(verify_token)):
    """
    Get the currently authenticated user's profile.
    """
    return UserProfile(id=user.id, email=user.email)
