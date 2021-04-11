# 291 A5 Task4
import sqlite3


def task4_sql(cursor):
    print("Task 4")
    try:
        sql = ''' SELECT *
        FROM reviews R, listings L
        WHERE R.comments =  "" AND R.listing_id = L.id
        ORDER BY listing_id ASC
        LIMIT 10'''
        cursor.execute(sql)
        result = cursor.fetchall()
        count = len(result)
        # check if there is data
        if count > 0:
            print("Accepted papers in this area: ")
            for i in result:
                for j in range(12):
                    print(i[j])
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
