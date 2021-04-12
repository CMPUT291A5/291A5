# 291 A5 Task 3
# Written by Bowen Xiao
# Find how many listings each host own, ordering the output by host_id and only output the top 10.
from pymongo import MongoClient
print("Task 3")
# open db
c = MongoClient()
db = c.A5db
collection = db.listings

lists = collection.aggregate([
    {"$group": {"_id": "$host_id", "count": {"$sum": 1}, "host_id": {
        "$first": "$host_id"}, "host_name": {"$first": "$host_name"}}},
    {"$project": {"_id": 0, "host_id": 1, "host_name": 1, "count": 1}},
    {"$sort": {"host_id": 1}},
    {"$limit": 10}])
# print result
for i in lists:
    print(i)
