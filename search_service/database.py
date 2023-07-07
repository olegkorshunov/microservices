from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from search_service.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.DATABASE_URL)


# create session and add objects
# with Session(engine) as session:
#     session.add(some_object)
#     session.add(some_other_object)
#     session.commit()
