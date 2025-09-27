from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    
    # Supabase Configuration
    supabase_url: str = Field(validation_alias="SUPABASE_URL")
    supabase_key: str = Field(validation_alias="SUPABASE_KEY")
    supabase_service_key: Optional[str] = Field(default=None, validation_alias="SUPABASE_SERVICE_KEY")
    
    # JWT Configuration
    jwt_secret: Optional[str] = "your-super-secret-jwt-key"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 30
    
    # Database
    database_url: Optional[str] = None
    
    # Environment
    environment: str = "development"
    debug: bool = True
    
    # Pydantic v2 settings configuration (replaces deprecated `class Config`)
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

# Global settings instance loaded from environment
# Static type checkers can't see env-based population; runtime construction without args is correct
settings = Settings()  # type: ignore