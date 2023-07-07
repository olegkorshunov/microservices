from datetime import date

from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column

from search_service.database import Base


class UserData(Base):
    __tablename__ = "user_data"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String)
    about: Mapped[str] = mapped_column(String)
    date_of_birdth: Mapped[date] = mapped_column(Date)
