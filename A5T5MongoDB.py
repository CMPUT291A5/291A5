# 291 A5 Task5 MongoDB
import pymongo
import time

def main():
    print("Task 5 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    mycoll = mydb["listings"]
    neighbourhood = input("Please enter neighbourhood:  ")

    start_time = time.time()
    for x in mycoll.aggregate([
            {
                '$match': {'neighbourhood': neighbourhood}
            },
            {
                '$group': {'_id': neighbourhood, 'rental_cost_avg': {'$avg': '$price'}}
            }
        ]):
        print(x)
    end_time = time.time()
    run_time = (end_time - start_time) * 1000
    print("Run time for Task 4 SQLite is:{}ms.".format(run_time))

main()
