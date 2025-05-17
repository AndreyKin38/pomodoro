import asyncio
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from settings import Settings


router = APIRouter(prefix="/ping",
                   tags=["ping"])


@router.get("/db")
async def ping_db():
    settings = Settings()

    return {"token": settings.GOOGLE_TOKEN_ID}


@router.get("/app")
async def ping_app():
    return {"text": "app is working"}