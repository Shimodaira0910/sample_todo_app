#from .db_connection import DbConnection
from .db_connection import DbConnection
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    user_name = Column('user_name', String(255))
    password = Column('password', String(255))
    
class UserDao:
    
    def __init__(self) -> None:
        self.session = DbConnection().session
    
    def create(self, user_name: str, password: str) -> bool:
        try:
            #ユーザー確認処理
            user = User(user_name=user_name, password=password)
            is_user_exists = self.is_user_exists(user)
            
            if is_user_exists is True:
                self.session.add(user)
                self.session.commit()
                print("ユーザー登録完了")
                return True
            else:
                print('存在するユーザーです。')
                return False
        except SQLAlchemyError as e:
            print(f'ユーザー作成時、エラーが発生しました。:{e}')
            self.session.rollback()
            return False
        finally:
            self.session.close()
    
    def delete(self, user_name:str) -> None:
        try:
            user = User(user_name=user_name)
            delete_user = self.session.query(User).filter_by(user_name=user.user_name).first()
            self.session.delete(delete_user)
            self.session.commit()
            return True 
        except SQLAlchemyError as e:
            print(f'ユーザー削除時、エラーが発生しました。:{e}')
            return False
        finally:
            self.session.close()
            
    def is_user_exists(self, user:User) -> bool:
        query_result = self.session.query(User).filter_by(user_name=user.user_name).first()
        if query_result is None:
            return True
        else:
            return False