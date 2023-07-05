from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

import auth_service.models  # noqa
from auth_service.auth.router import router as auth_router
from auth_service.database import Base, async_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    async with async_engine.begin() as conn:
        from auth_service import models
        await conn.run_sync(Base.metadata.create_all)

    yield
    # SHUTDOWN


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
