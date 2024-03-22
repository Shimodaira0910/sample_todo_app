from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pymysql

pymysql.install_as_MySQLdb()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = os.getenv("DB_NAME")

class DbConnection:
    
    def __init__(self) -> None:
        self._DB_URL = self.generate_db_url()
        self.session = self.db_connection()

    def generate_db_url(self):
        DB_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
        return DB_URL

    def db_connection(self) -> sessionmaker:
        DATABASE_URL = self._DB_URL
        engine = create_engine(DATABASE_URL)
        
        SessionClass = sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False
            )
        
        session = SessionClass()
        return session
