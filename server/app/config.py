from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str | None = None
    
    groq_api_key: str | None = None
    serper_api_key: str | None = None
    newsapi_key: str | None = None
    
    redis_url: str = "redis://redis:6379/0"
    
    searxng_url: str = "http://searxng:8080"
    
    freshrss_url: str = "http://freshrss:80"
    freshrss_api_password: str | None = None
    
    app_env: str = "development"
    app_debug: bool = True
    cors_origins: str = "http://localhost:3000"
    
    max_upload_size_mb: int = 50
    file_retention_hours: int = 24
    rate_limit_fact_check: int = 10
    rate_limit_image_check: int = 20
    rate_limit_text_check: int = 30
    
    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
