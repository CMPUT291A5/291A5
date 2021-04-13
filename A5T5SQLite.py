# 291 A5 Task5 SQLite
import sqlite3
import sys


def task5_sql(cursor):
    print("Task 5 SQLite")
    if len(sys.argv) > 1:
        neighbourhood = str(sys.argv[1])
    else:
        neighbourhood = input("Please enter a neighbourhood: ")

    try:
        sql = ''' SELECT avg(price) as average_rental
        FROM listings
        WHERE neighbourhood = :Neighbourhood
        '''
        cursor.execute(sql, {'Neighbourhood': neighbourhood})
        result = cursor.fetchall()
        count = len(result)
        # check if there is data
        if count > 0:
            print("The average price per night of ", neighbourhood, "is: ")
            for i in result:
                print(int(i[0]))

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
