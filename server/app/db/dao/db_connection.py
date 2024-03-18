from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(dirname(dirname(__file__))), '.env')
load_dotenv(dotenv_path)

# MySQLへの接続情報
DATABASE = os.environ.get("DATABASE")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
DB_NAME = os.environ.get("DB_NAME")


class DbConnection:
    
    def __init__(self) -> None:
        self.session = self.db_connection()

    def db_connection(self) -> sessionmaker:
        DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
        engine = create_engine(DATABASE_URL)
        SessionClass = sessionmaker(engine)
        session = SessionClass()
        return session
