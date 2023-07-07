from datetime import date

from faker import Faker
from sqlalchemy import Date, String, create_engine, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


fake = Faker()


class UserData(Base):
    __tablename__ = "user_data"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String)
    about: Mapped[str] = mapped_column(String)
    date_of_birdth: Mapped[date] = mapped_column(Date)


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/user_data")

with Session(engine) as session:
    for _ in range(10):
        data = {
            "name": fake.name(),
            "city": fake.city(),
            "about": fake.text(),
            "date_of_birdth": fake.date(),
        }
        query = insert(UserData).values(**data)
        session.execute(query)
        session.commit()
