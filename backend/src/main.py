from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import tasks
from src.config.database import create_db_and_tables
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler to initialize database tables on startup."""
    create_db_and_tables()
    yield


app = FastAPI(
    title="FastAPI Todo Backend Service",
    version="1.0.0",
    lifespan=lifespan,
    description="A secure, user-scoped task management API with JWT authentication"
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint to verify the application is running."""
    return {"status": "healthy", "service": "FastAPI Todo Backend"}


@app.get("/")
async def root():
    """Root endpoint to provide information about all available routes."""
    return {
        "routes": [
            {"path": "/", "description": "Root endpoint with available routes."},
            {"path": "/health", "description": "Health check endpoint."},
            {"path": "/tasks", "description": "Task-related operations."}
        ],
        "documentation_url": "/docs"
    }


# Include API routes
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


# Add global exception handlers
@app.exception_handler(500)
async def internal_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)