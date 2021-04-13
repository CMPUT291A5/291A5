# 291 A5 Task5 SQLite
import sqlite3
import time

def task5_sql(cursor):
    print("Task 5 SQLite")
    neighbourhood = input("Please enter neighbourhood:  ")
    start_time = time.time()
    try:
        sql = ''' SELECT avg(price) as average_rental
        FROM listings
        WHERE neighbourhood = :Neighbourhood
        '''
        cursor.execute(sql, {'Neighbourhood': neighbourhood})
        end_time = time.time()
        run_time = (end_time - start_time)* 1000
        result = cursor.fetchall()
        count = len(result)
        # check if there is data
        if count > 0:
            for i in result:
                print(int(i[0]))
            print("Run time for Task 5 SQLite is:{}ms.".format(run_time))
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
    task5_sql(c)
    print("\n")
    conn.close()


main()
