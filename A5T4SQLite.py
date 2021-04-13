# 291 A5 Task4 SQLite
import sqlite3
import time

def task4_sql(cursor):
    print("Task 4 SQLite")
    start_time = time.time()
    try:
        sql = ''' SELECT *
        FROM reviews 
        WHERE comments =  "" 
        ORDER BY listing_id ASC
        LIMIT 10'''
        cursor.execute(sql)
        end_time = time.time()
        run_time = (end_time - start_time)* 1000
        result = cursor.fetchall()
        count = len(result)
        # check if there is data
        if count > 0:
            print("The listing_id is:")
            for i in result:
              print(i[0])
            print("Run time for Task 4 SQLite is:{}ms.".format(run_time))
        else:
            print("None of them fit.\n")

    except Exception as e:
        # the error will show  if exists
        print(e)
        print('cannot query')


def main():
    conn = sqlite3.connect('./A5.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    task4_sql(c)
    print("\n")
    conn.close()


main()
