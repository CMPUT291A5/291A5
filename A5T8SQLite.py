# 291 A5 Task 8
import sqlite3
import sys


def task8(c):
    # Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.
    # useing command line prompt or via an application parameter
    if len(sys.argv) > 1:
        listing_id = sys.argv[1]
    else:
        listing_id = input("Please enter a listing id: ")

    try:
        sql = '''SELECT l.host_name,l.price, r.date, r.comments
FROM listings l, reviews r
WHERE l.id = :listing_id AND l.id = r.listing_id 
ORDER BY r.date DESC  LIMIT 0,1
'''
        c.execute(sql, {'listing_id': listing_id})
        rows = c.fetchall()
        count = len(rows)
        if count > 0:
            # find result
            for i in rows:
                print(i[0], i[1], i[2], i[3])
        else:
            print("Not exist")

    except Exception as e:
        # the erro will show if exists
        print(e)
        print("cannot query")


def main():
    # open database
    conn = sqlite3.connect('./A5.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    print("Task 8")
    # execute
    task8(c)
    conn.close()


main()
