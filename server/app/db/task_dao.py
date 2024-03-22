from .db_connection import DbConnection
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, DATE
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Task(Base):
    __tablename__ = 'Task'
    task_id = Column('task_id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, ForeignKey('User.user_id'))
    task_name = Column('task_name', String)
    due_date = Column('due_date', DATE)
    priority = Column('priority', Integer)
    
class TaskDao:
    
    def __init__(self) -> None:
        self.session = DbConnection().session
    
    def create(self, user_id: int, task_name: str, due_date, priority: int) -> bool:
        try:
            task = Task(user_id=user_id, task_name=task_name, due_date=due_date, priority=priority)
            self.session.add(task)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            print(f'タスク作成時、エラーが発生しました。:{e}')
            self.session.rollback()
            return False
        finally:
            self.session.close()