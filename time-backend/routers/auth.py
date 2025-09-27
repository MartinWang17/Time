from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database import get_supabase
from models import UserCreate, UserLogin, Token, User
from typing import Optional

router = APIRouter()
security = HTTPBearer()

@router.post("/signup", response_model=dict)
async def signup(user: UserCreate):
    """Create a new user account"""
    try:
        supabase = get_supabase()
        
        # Create user with Supabase Auth
        response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "data": {
                "full_name": user.full_name
            }
        })
        
        if response.user:
            return {
                "message": "User created successfully. Please check your email to verify your account.",
                "user_id": response.user.id
            }
        else:
            raise HTTPException(status_code=400, detail="Failed to create user")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    """Authenticate user and return access token"""
    try:
        supabase = get_supabase()
        
        # Sign in with Supabase Auth
        response = supabase.auth.sign_in_with_password({
            "email": user_login.email,
            "password": user_login.password
        })
        
        if response.session and response.session.access_token:
            return Token(
                access_token=response.session.access_token,
                token_type="bearer",
                expires_in=response.session.expires_in or 3600
            )
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
            
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Logout user and invalidate token"""
    try:
        supabase = get_supabase()
        supabase.auth.sign_out()
        return {"message": "Successfully logged out"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me", response_model=dict)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user information"""
    try:
        supabase = get_supabase()
        
        # Set the session token
        supabase.auth.set_session(credentials.credentials)
        
        # Get user info
        user = supabase.auth.get_user()
        
        if user.user:
            return {
                "id": user.user.id,
                "email": user.user.email,
                "full_name": user.user.user_metadata.get("full_name"),
                "created_at": user.user.created_at
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
            
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Dependency to get current user ID from token"""
    try:
        supabase = get_supabase()
        
        # Set the session token
        supabase.auth.set_session(credentials.credentials)
        
        # Get user info
        user = supabase.auth.get_user()
        
        if user.user:
            return user.user.id
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
            
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")