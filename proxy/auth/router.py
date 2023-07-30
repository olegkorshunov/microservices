from fastapi import APIRouter, Request

from proxy.auth.schemas import SUserInfo, SUserLogin, SUserRegister
from proxy.reverse_proxy import ReverseProxy

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"],
)


reverse_proxy = ReverseProxy(host="127.0.0.1", port="4000")


@router.post("/register")
async def register_user(request: Request, user_data: SUserRegister):
    return await reverse_proxy(request)


@router.post("/login")
async def login_user(request: Request, user_data: SUserLogin):
    return await reverse_proxy(request)


@router.post("/logout")
async def logout_user(request: Request):
    return await reverse_proxy(request)


@router.get("/is_auth")
async def get_user_info(request: Request) -> SUserInfo:
    return await reverse_proxy(request)
