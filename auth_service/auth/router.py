from fastapi import APIRouter, Depends, Response

import auth_service.exceptions as HttpException
from auth_service.auth.auth import authenticate_user, create_access_token, get_password_hash
from auth_service.auth.constants import access_token
from auth_service.auth.dao import DaoAuth
from auth_service.auth.dependencies import get_current_user
from auth_service.auth.schemas import SUserInfo, SUserLogin, SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existig_user = await DaoAuth.find_one_or_none(email=user_data.email)
    if existig_user:
        raise HttpException.UserAlredyExist
    hashed_password = get_password_hash(password=user_data.password)
    await DaoAuth.insert(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token_jwt = create_access_token({"sub": str(user.id)})
    response.set_cookie(access_token, access_token_jwt)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(access_token)


@router.get("/is_auth")
async def get_user_info(user: SUserInfo = Depends(get_current_user)) -> SUserInfo:
    return user