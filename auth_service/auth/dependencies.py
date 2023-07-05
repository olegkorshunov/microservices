from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

import auth_service.exceptions as HttpException
from auth_service.auth.constants import access_token
from auth_service.auth.dao import DaoAuth
from auth_service.config import settings


def get_access_token(request: Request):
    access_token_jwt = request.cookies.get(access_token)
    if not access_token_jwt:
        raise HttpException.TokenAbsent
    return access_token_jwt


async def get_current_user(access_token_jwt: str = Depends(get_access_token)):
    try:
        payload = jwt.decode(access_token_jwt, settings.SECRET_KEY_jwt, algorithms=settings.ALGORITHM)
    except JWTError:
        raise HttpException.IncorrectTokenFormat
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise HttpException.AuthTokenExpier
    user_id = payload.get("sub")
    if not user_id:
        raise HttpException.UserDataNotFound
    user = await DaoAuth.find_one_by_id(int(user_id))
    if not user:
        raise HttpException.UserDataNotFound
    return user
