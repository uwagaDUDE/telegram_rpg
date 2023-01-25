
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='postgres', user='postgres', password=os.environ.get("SQL_PASSWORD"), host='localhost',port=5432)
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')