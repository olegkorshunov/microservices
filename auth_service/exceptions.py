from fastapi import HTTPException, status


class AuthException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlredyExist(AuthException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("User alredy exist",)


class IncorrectEmailOrPassword(AuthException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Incorrect email or password",)


class AuthTokenExpier(AuthException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Auth token has expired",)


class TokenAbsent(AuthException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Token is absent",)


class IncorrectTokenFormat(AuthException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Incorrect token format",)