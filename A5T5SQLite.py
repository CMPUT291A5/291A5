# 291 A5 Task5
import sqlite3


def task5_sql(cursor):
    print("Task 5")
    neighbourhood = input("Please enter neighbourhood:  ")
    run_time = input("Please enter run-time: ")

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
            for i in result:
                print(int(i[0]))
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
