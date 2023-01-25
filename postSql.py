
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class DataBase:
    def __init__(self, dbname, user, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = os.environ.get("SQL_PASSWORD")
        self.host = host
        self.port = port
        self.cursor = None

    def connect(self):
        try:
            conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                                    password=self.password, host=self.host, port=self.port)
            self.cursor = conn.cursor()
        except Exception():
            print(Exception())


