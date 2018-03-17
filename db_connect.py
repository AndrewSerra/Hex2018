import sqlite3

conn = sqlite3.connect('politics.db')

try:
    c = conn.cursor()
    # create table
    create_table_sql = '''
                           create table tweets
                           (tweet text, location text, follower_count)
                       '''
    c.execute(create_table_sql)

    # save the table
    conn.commit()
    conn.close()

except:
    pass

def insert_row(tweet, loc, f_count):
    conn1 = sqlite3.connect('politics.db')
    c_row = conn1.cursor()
    query = "insert into tweets values (?,?,?)"
    c_row.execute(query, (tweet, loc, f_count))
    conn1.commit()
