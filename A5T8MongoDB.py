# 291 A5 Task 8
# Written by Bowen Xiao
# Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.
from pymongo import MongoClient
import sys

print("Task 8")
# open db
c = MongoClient()
db = c.A5db
collection = db.listings

# useing command line prompt or via an application parameter
if len(sys.argv) > 1:
    myinput = int(sys.argv[1])
else:
    myinput = int(input("Please enter a listing id: "))

lists = collection.aggregate([
    {"$lookup": {"from": "reviews", "localField": "id",
                 "foreignField": "listing_id", "as": "list_view"}},
    {"$match": {"id": myinput}},
    {"$project": {"_id": 0, "host_name": 1, "price": 1,
                  "list_view.date": 1, "list_view.comments": 1}},
    {"$unwind": "$list_view"},
    {"$sort": {"list_view.date": -1}},
    {"$limit": 1}])
# print result
for i in lists:
    print(i)
