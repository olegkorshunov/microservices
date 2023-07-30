from datetime import date

from pydantic import BaseModel


class SUserData(BaseModel):
    name: str
    city: str | None
    about: str | None
    date_of_birdth: date | None
