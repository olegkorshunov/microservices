from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from proxy.auth.router import router as auth_router
from proxy.search.router import router as search_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(search_router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
