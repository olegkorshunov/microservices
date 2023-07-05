from auth_service.auth.models import UserAccount
from auth_service.dao.daobase import DaoBase


class DaoAuth(DaoBase[UserAccount]):
    model = UserAccount