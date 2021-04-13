
# 291 A5 Task5 MongoDB
import pymongo
import sys

def main():
    print("Task 5 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    mycoll = mydb["listings"]
    neighbourhood = str(sys.argv[1])

    x = mycoll.aggregate([
        {
            '$match': {'neighbourhood': neighbourhood}
        },
        {
            '$group': {'_id': neighbourhood, 'rental_cost_avg': {'$avg': '$price'}}
        }
    ])
    # change the float to int
    for i in x:
        print('The average price in', neighbourhood, int(i['rental_cost_avg']), '$')



main()
