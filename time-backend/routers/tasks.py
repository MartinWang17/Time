from fastapi import APIRouter, HTTPException, Depends, Query
from database import get_supabase
from models import (
    TaskCreate, TaskUpdate, TaskResponse, TaskListResponse, 
    TaskStatus, TaskPriority, CategoryCreate, Category, CategoryListResponse
)
from routers.auth import get_current_user_id
from typing import Optional, List
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def create_task(
    task: TaskCreate, 
    user_id: str = Depends(get_current_user_id)
):
    """Create a new task"""
    try:
        supabase = get_supabase()
        
        task_data = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority.value,
            "status": "todo",
            "due_date": task.due_date.isoformat() if task.due_date else None,
            "category": task.category,
            "tags": task.tags or [],
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        response = supabase.table("tasks").insert(task_data).execute()
        
        if response.data:
            return TaskResponse(**response.data[0])
        else:
            raise HTTPException(status_code=400, detail="Failed to create task")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/tasks", response_model=TaskListResponse)
async def get_tasks(
    user_id: str = Depends(get_current_user_id),
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    category: Optional[str] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=100)
):
    """Get user's tasks with optional filtering"""
    try:
        supabase = get_supabase()
        
        query = supabase.table("tasks").select("*").eq("user_id", user_id)
        
        # Apply filters
        if status:
            query = query.eq("status", status.value)
        if priority:
            query = query.eq("priority", priority.value)
        if category:
            query = query.eq("category", category)
            
        # Apply pagination
        offset = (page - 1) * per_page
        query = query.range(offset, offset + per_page - 1)
        
        # Order by created_at desc
        query = query.order("created_at", desc=True)
        
        response = query.execute()
        
        # Get total count
        count_response = supabase.table("tasks").select("id", count="exact").eq("user_id", user_id).execute()
        total = count_response.count or 0
        
        tasks = [TaskResponse(**task) for task in response.data] if response.data else []
        
        return TaskListResponse(
            tasks=tasks,
            total=total,
            page=page,
            per_page=per_page
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: str, 
    user_id: str = Depends(get_current_user_id)
):
    """Get a specific task by ID"""
    try:
        supabase = get_supabase()
        
        response = supabase.table("tasks").select("*").eq("id", task_id).eq("user_id", user_id).execute()
        
        if response.data and len(response.data) > 0:
            return TaskResponse(**response.data[0])
        else:
            raise HTTPException(status_code=404, detail="Task not found")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str,
    task_update: TaskUpdate,
    user_id: str = Depends(get_current_user_id)
):
    """Update a task"""
    try:
        supabase = get_supabase()
        
        # Check if task exists and belongs to user
        existing_task = supabase.table("tasks").select("*").eq("id", task_id).eq("user_id", user_id).execute()
        
        if not existing_task.data:
            raise HTTPException(status_code=404, detail="Task not found")
        
        # Prepare update data
        update_data = {"updated_at": datetime.utcnow().isoformat()}
        
        if task_update.title is not None:
            update_data["title"] = task_update.title
        if task_update.description is not None:
            update_data["description"] = task_update.description
        if task_update.priority is not None:
            update_data["priority"] = task_update.priority.value
        if task_update.status is not None:
            update_data["status"] = task_update.status.value
            if task_update.status == TaskStatus.COMPLETED:
                update_data["completed_at"] = datetime.utcnow().isoformat()
        if task_update.due_date is not None:
            update_data["due_date"] = task_update.due_date.isoformat()
        if task_update.category is not None:
            update_data["category"] = task_update.category
        if task_update.tags is not None:
            update_data["tags"] = task_update.tags
        
        response = supabase.table("tasks").update(update_data).eq("id", task_id).eq("user_id", user_id).execute()
        
        if response.data:
            return TaskResponse(**response.data[0])
        else:
            raise HTTPException(status_code=400, detail="Failed to update task")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: str, 
    user_id: str = Depends(get_current_user_id)
):
    """Delete a task"""
    try:
        supabase = get_supabase()
        
        response = supabase.table("tasks").delete().eq("id", task_id).eq("user_id", user_id).execute()
        
        if response.data:
            return {"message": "Task deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Task not found")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Category endpoints
@router.post("/categories", response_model=Category)
async def create_category(
    category: CategoryCreate,
    user_id: str = Depends(get_current_user_id)
):
    """Create a new category"""
    try:
        supabase = get_supabase()
        
        category_data = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "name": category.name,
            "description": category.description,
            "color": category.color,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        response = supabase.table("categories").insert(category_data).execute()
        
        if response.data:
            return Category(**response.data[0])
        else:
            raise HTTPException(status_code=400, detail="Failed to create category")
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/categories", response_model=CategoryListResponse)
async def get_categories(user_id: str = Depends(get_current_user_id)):
    """Get user's categories"""
    try:
        supabase = get_supabase()
        
        response = supabase.table("categories").select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
        
        categories = [Category(**cat) for cat in response.data] if response.data else []
        
        return CategoryListResponse(
            categories=categories,
            total=len(categories)
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))