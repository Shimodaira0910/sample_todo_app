#from .db_connection import DbConnection
from .db_connection import DbConnection
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    user_name = Column('user_name', String(255), unique=True)
    password = Column('password', String(255), )
    
class UserDao:
    
    def __init__(self) -> None:
        self.session = DbConnection().session
    
    def create(self, user_name: str, password: str) -> bool:
        try:
            user = User(user_name=user_name, password=password)
            self.session.add(user)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            print(f'ユーザー作成時、エラーが発生しました。:{e}')
            return False
    
    def delete(self, user_name:str) -> None:
        try:
            user = User(user_name=user_name)
            delete_user = self.session.query(User).filter_by(name=user.user_name).first()
            self.session.delete(delete_user)
            self.session.commit()
            return True 
        except SQLAlchemyError as e:
            print(f'ユーザー作成時、エラーが発生しました。:{e}')
            return False
            