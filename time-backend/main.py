from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from config import settings
from database import init_supabase
from routers import auth, tasks

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    print("Starting up Task Tracker API...")
    init_supabase()
    yield
    # Shutdown
    print("Shutting down Task Tracker API...")

# Initialize FastAPI app
app = FastAPI(
    title="Task Tracker API",
    description="A FastAPI backend for task management with Supabase integration",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(tasks.router, prefix="/api", tags=["tasks"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Task Tracker API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )