# 291 A5 Task4 MongoDB

import pymongo
import time

def main():
    print("Task 4 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    mycoll = mydb["reviews"]
    start_time = time.time()
    for x in mycoll.find({"comments":  ""},{"_id": 0, "comments": 0}).limit(10).sort([('Listing_id', 1)]):

        print(x)
    end_time = time.time()
    run_time = (end_time - start_time) * 1000
    print("Run time for Task 4 MongoDB is:{}ms.".format(run_time))
main()
