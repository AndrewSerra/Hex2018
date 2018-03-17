import sqlite3

conn = sqlite3.connect('politics.db')

try:
    c = conn.cursor()
    # create table
    create_table_sql = '''
                           create table tweets
                           (tweet text, location text, follower_count integer)
                       '''
    c.execute(create_table_sql)

    # save the table
    conn.commit()

except:
    pass

def get_db_connection():

    return conn

def insert_row(tweet, loc, f_count, c):

    query = "insert into tweets values(" + tweet + "," + loc + "," + f_count + ")"
    c.execute(query)
