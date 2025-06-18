from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import log_fiber_splice
import uvicorn
import os

app = FastAPI(
    title="PML MCP Fiber Tracker",
    description="API for tracking and managing fiber optic infrastructure deployments",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(log_fiber_splice.router, tags=["splice-operations"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "pml-fiber-tracker"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=debug
    )
