from dotenv import load_dotenv, find_dotenv
import mysql.connector
import os

#locate the .env file
load_dotenv(find_dotenv())

db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

my_cursor = db.cursor()
