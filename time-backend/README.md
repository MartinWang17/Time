# Task Tracker API Backend

A FastAPI backend for the "time" task management application with Supabase integration.

## Features

- **Task Management**: Create, read, update, and delete tasks
- **Categories**: Organize tasks with custom categories
- **User Authentication**: Secure authentication via Supabase Auth
- **Priority Levels**: Set task priorities (Low, Medium, High, Urgent)
- **Status Tracking**: Track task status (Todo, In Progress, Completed, Cancelled)
- **Due Dates**: Set and manage task deadlines
- **Tags**: Add tags to tasks for better organization
- **Pagination**: Efficient task listing with pagination
- **Filtering**: Filter tasks by status, priority, and category

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Supabase**: Backend-as-a-Service for database and authentication
- **Pydantic**: Data validation and settings management
- **Python 3.13+**: Latest Python version

## Project Structure

```
time-backend/
├── main.py                 # FastAPI application entry point
├── config.py              # Application configuration
├── database.py           # Supabase connection and database utilities
├── models.py             # Pydantic models for data validation
├── routers/              # API route handlers
│   ├── __init__.py
│   ├── auth.py          # Authentication endpoints
│   └── tasks.py         # Task management endpoints
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
├── start_dev.sh        # Development server startup script
└── README.md           # This file
```

## Setup Instructions

### 1. Prerequisites

- Python 3.9 or higher
- A Supabase account and project

### 2. Clone and Setup

```bash
cd time-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Supabase Setup

1. Create a new Supabase project at [https://supabase.com](https://supabase.com)
2. In your Supabase dashboard, go to Settings > API
3. Copy your Project URL and anon key
4. Create the following tables in your Supabase database:

#### Tasks Table

```sql
CREATE TABLE tasks (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    status TEXT NOT NULL DEFAULT 'todo' CHECK (status IN ('todo', 'in_progress', 'completed', 'cancelled')),
    due_date TIMESTAMP WITH TIME ZONE,
    category TEXT,
    tags TEXT[] DEFAULT '{}',
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Row Level Security
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own tasks" ON tasks
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own tasks" ON tasks
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own tasks" ON tasks
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own tasks" ON tasks
    FOR DELETE USING (auth.uid() = user_id);
```

#### Categories Table

```sql
CREATE TABLE categories (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    color TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, name)
);

-- Row Level Security
ALTER TABLE categories ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own categories" ON categories
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own categories" ON categories
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own categories" ON categories
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own categories" ON categories
    FOR DELETE USING (auth.uid() = user_id);
```

### 4. Environment Configuration

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Supabase credentials:
```env
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key  # Optional
```

### 5. Run the Application

#### Option 1: Using the startup script
```bash
./start_dev.sh
```

#### Option 2: Direct command
```bash
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/signup` - Create a new user account
- `POST /auth/login` - Login and get access token
- `POST /auth/logout` - Logout user
- `GET /auth/me` - Get current user information

### Tasks
- `GET /api/tasks` - List tasks with filtering and pagination
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{task_id}` - Get a specific task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task

### Categories
- `GET /api/categories` - List user categories
- `POST /api/categories` - Create a new category

### Health Check
- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint

## Authentication

The API uses Bearer token authentication. Include the JWT token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## Usage Examples

### Create a Task
```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs",
    "priority": "high",
    "due_date": "2024-01-15T10:00:00Z",
    "category": "Work",
    "tags": ["documentation", "urgent"]
  }'
```

### Get Tasks
```bash
curl "http://localhost:8000/api/tasks?status=todo&priority=high&page=1&per_page=10" \
  -H "Authorization: Bearer <your-token>"
```

## Development

### Code Structure
- All models are defined in `models.py` using Pydantic
- Route handlers are organized in the `routers/` directory
- Database operations use the Supabase Python client
- Authentication is handled by Supabase Auth

### Adding New Features
1. Define new Pydantic models in `models.py`
2. Create route handlers in appropriate router files
3. Update database schema in Supabase if needed
4. Add appropriate RLS policies for security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is licensed under the MIT License.