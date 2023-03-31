from fastapi import FastAPI

from api.v1.health.controller import router as health_router

app = FastAPI()

app.include_router(health_router)
