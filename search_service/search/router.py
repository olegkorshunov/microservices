from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs
from sqlalchemy import select
from sqlalchemy.orm import Session

from search_service.database import engine
from search_service.search.models import UserData
from search_service.search.schemas import SUserData

blueprint = Blueprint("search", __name__)


@blueprint.route("/", methods=["POST"])
@use_kwargs(SUserData)
@marshal_with(SUserData(many=True))
def search(**kwargs):
    with Session(engine) as session:
        query = select(UserData).filter_by(**kwargs)
        result = session.scalars(query).all()
    return result
