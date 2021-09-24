import mysql.connector
import config

# conn = mysql.connector.connect(
#     host='localhost',
#     port='3306',
#     user='root',
#     password=config.PASSWORD
# )

# cursor = conn.cursor()

# sql = """create database movie"""
#
# cursor.execute(sql)

conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password=config.PASSWORD,
    database='movie'
)

cursor = conn.cursor()

# sql = """create table movie(
#         id int auto_increment primary key,
#         name varchar(255),
#         duration int,
#         director varchar(255),
#         year date,
#         cast text)"""
#
# cursor.execute(sql)

sql = """INSERT INTO movie(name, duration, director, year, cast) values
        ('Titanic', 180, 'James Cameron', '1998-01-01', 'Leo Di Caprio')"""


sql = """UPDATE movie SET duration = 200 WHERE name = 'Gentlemen'"""

# cursor.execute(sql)
# conn.commit()

sql = """SELECT * FROM movie"""

cursor.execute(sql)
res = cursor.fetchall()
print(res)


