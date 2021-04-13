# 291 A5 Task 3
# Written by Bowen Xiao
import sqlite3


def task3(c):
    # Find how many listings each host own, ordering the output by host_id and only output the top 10.
    try:
        sql = '''SELECT c, host_id, host_name
FROM(SELECT COUNT(*) AS c, host_id, host_name
FROM listings l
GROUP BY l.host_id
ORDER BY COUNT(*) DESC LIMIT 10)
ORDER BY host_id'''
        c.execute(sql)
        rows = c.fetchall()
        # find result
        for i in rows:
            print(i[0], i[1], i[2])

    except Exception as e:
        # the erro will show if exists
        print(e)
        print("cannot query")


def main():
    # open database
    conn = sqlite3.connect('./A5.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    print("Task 3")
    # execute
    task3(c)
    conn.close()


main()
