#from .db.dao.user_dao import UserDao
#from ..db.dao.user_dao import UserDao
from ..db.user_dao import UserDao


class UserService:
    
    def __init__(self) -> None:
        self._user_dao = UserDao()
    
    def register_user(self, username: str, password: str):
        #TODO ここにパスワードハッシュ化アルゴリズムを追加したい
        register_result = self._user_dao.create(username, password)
        if register_result is None:
            return {'result':'No'}
        else:
            return {'result':'Ok'}