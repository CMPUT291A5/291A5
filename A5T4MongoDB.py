# 291 A5T4MongoDB

import pymongo


def main():
    print("Task 4")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    mycoll = mydb["reviews"]
    for x in mycoll.find({"comments":  ""},{"_id": 0, "comments": 0}).limit(10).sort([('Listing_id', 1)]):
        print(x)

main()
