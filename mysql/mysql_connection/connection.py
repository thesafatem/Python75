import mysql.connector
import config

sql = """create table movie(
        id int auto_increment primary key,
        name varchar(255),
        duration int,
        director varchar(255),
        year date,
        cast text)"""

sql = """insert into movie(name, duration, director, year, cast) values
        ('Titanic', 180, 'James Cameron', '1998-01-01', 'Leo di Caprio'),
        ('Avatar', 200, 'James Cameron', '2010-09-09', 'Sigurney Weaver'),
        ('Duna', 160, 'Deni Vilneuve', '2021-09-15', 'Timoti Shalame')"""

sql = """select * from movie"""

sql = """select name from movie where year >= '2009-01-01'"""

director = 'James Cameron'

sql = f"""select * from movie where director = '{director}'"""

duration = 200

sql = """select * from movie where duration < %s"""
# cursor.execute(sql, (duration,))

# cursor.execute(sql)
# res = cursor.fetchall()
# print(res)
# conn.commit()


def get_conn(database_name):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password=config.PASSWORD,
            database=database_name
        )
        return conn
    except mysql.connector.Error as e:
        raise e


def create_table(database_name, sql):
    try:
        conn = get_conn(database_name)
        cursor = conn.cursor()
        cursor.execute(sql)
    except mysql.connector.Error as e:
        print(e)

# columns = ('name', 'director', 'year', 'cast')
# columns_text = 'name, director, year, cast'
# s_list = ['%s', '%s', '%s', '%s']
# '%s, %s, %s, %s'


def insert_row(database_name, table_name, columns, values):
    try:
        conn = get_conn(database_name)
        cursor = conn.cursor()
        columns_str = ','.join(columns)
        s_list = ['%s' for i in range(len(columns))]
        s_str = ','.join(s_list)
        sql = f"""insert into {table_name}({columns_str}) values
                ({s_str})"""
        cursor.execute(sql, values)
        conn.commit()
        sql = """select last_insert_id()"""
        cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)


def delete_table(database_name, table_name):
    try:
        conn = get_conn(database_name)
        cursor = conn.cursor()
        sql = f"""drop table {table_name}"""
        cursor.execute(sql)
    except mysql.connector.Error as e:
        print(e)


# delete_table('python75', 'movie')
# create_table('python75',
#              """create table movie(
#                 id int auto_increment primary key,
#                 name varchar(255),
#                 duration int,
#                 director varchar(255),
#                 year date,
#                 cast text)""")

res = insert_row(
    'python75',
    'movie',
    ('name', 'duration', 'director', 'year', 'cast'),
    ('Avatar', 200, 'James Cameron', '2010-09-09', 'Sigurney Weaver')
)
print(res)




