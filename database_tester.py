from posix import XATTR_SIZE_MAX
from dotenv import load_dotenv, find_dotenv
import mysql.connector
import os

#locate the .env file
load_dotenv(find_dotenv())

#Configure the database connection using environment variables
db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

my_cursor = db.cursor()

#my_cursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#my_cursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Rob",32))
#db.commit()
my_cursor.execute("SELECT * FROM Person")

for x in my_cursor:
    print(x)