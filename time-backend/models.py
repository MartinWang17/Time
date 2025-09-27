from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import Enum

class TaskStatus(str, Enum):
    """Task status enum"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskPriority(str, Enum):
    """Task priority enum"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class TaskBase(BaseModel):
    """Base task model"""
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = []
    
class TaskCreate(TaskBase):
    """Task creation model"""
    pass
    
class TaskUpdate(BaseModel):
    """Task update model"""
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class Task(TaskBase):
    """Complete task model"""
    id: str
    user_id: str
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class TaskResponse(BaseModel):
    """Task response model"""
    id: str
    title: str
    description: Optional[str] = None
    priority: TaskPriority
    status: TaskStatus
    due_date: Optional[datetime] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = []
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None

# Category models
class CategoryBase(BaseModel):
    """Base category model"""
    name: str
    description: Optional[str] = None
    color: Optional[str] = None  # Hex color code

class CategoryCreate(CategoryBase):
    """Category creation model"""
    pass

class Category(CategoryBase):
    """Complete category model"""
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# User models for authentication
class UserBase(BaseModel):
    """Base user model"""
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    """User creation model"""
    password: str

class User(UserBase):
    """Complete user model"""
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    """User login model"""
    email: str
    password: str

class Token(BaseModel):
    """JWT token model"""
    access_token: str
    token_type: str
    expires_in: int

class TokenData(BaseModel):
    """Token data model"""
    user_id: Optional[str] = None

# Response models
class TaskListResponse(BaseModel):
    """Task list response model"""
    tasks: List[TaskResponse]
    total: int
    page: int
    per_page: int

class CategoryListResponse(BaseModel):
    """Category list response model"""
    categories: List[Category]
    total: int