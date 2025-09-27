from supabase import create_client, Client
from config import settings
from typing import Optional

# Global Supabase client instance
supabase: Optional[Client] = None

def init_supabase() -> Client:
    """Initialize Supabase client"""
    global supabase
    
    if not supabase:
        supabase = create_client(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key
        )
    
    return supabase

def get_supabase() -> Client:
    """Get Supabase client instance"""
    if not supabase:
        return init_supabase()
    return supabase

async def create_tables():
    """Create necessary tables if they don't exist"""
    client = get_supabase()
    
    # Note: In a real application, you would typically use Supabase migrations
    # or SQL scripts to create tables. This is just for demonstration.
    
    # Time entries table creation would be handled by Supabase migrations
    # For now, we'll assume the tables are created via Supabase dashboard
    
    print("Tables should be created via Supabase dashboard or migrations")
    return True