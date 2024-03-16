from ..db.dao.user_dao import UserDao

class UserService:
    
    def __init__(self) -> None:
        self.user_dao = UserDao()
    
    def register_user(self ,username: str, password: str):
        #TODO ここにパスワードハッシュ化アルゴリズムを追加したい
        register_result = self.user_dao.create(username, password)
        if register_result is None:
            return {'result':'No'}
        else:
            return {'result':'Ok'}