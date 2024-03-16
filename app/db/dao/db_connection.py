from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(dirname(__file__), '.env'))
load_dotenv(dotenv_path)

# MySQLへの接続情報
DATABASE = os.environ("DATABASE")
USER = os.environ("USER")
PASSWORD = os.environ("PASSWORD")
HOST = os.environ("HOST")
PORT = os.environ("PORT")
DB_NAME = os.environ("DB_NAME")


class DbConnection:
    
    def __init__(self) -> None:
        self._session = self.db_connection()

    def db_connection(self) -> sessionmaker:
        DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
        engine = create_engine(DATABASE_URL)
        SessionClass = sessionmaker(engine)
        session = SessionClass()
        return session
