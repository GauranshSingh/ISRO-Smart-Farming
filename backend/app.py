from fastapi import FastAPI

from backend.routes import router

app = FastAPI(
    title="ISRO Smart Farming API",
    version="1.0"
)

app.include_router(router)