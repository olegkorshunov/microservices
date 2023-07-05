from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from auth_service.database import Base


class UserAccount(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.email}"