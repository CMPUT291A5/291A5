
import pymongo


def main():
    print("Task 5 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    mycoll = mydb["listings"]
    neighbourhood = input("Please enter neighbourhood:  ")
    run_time = input("Please enter run-time: ")

    for x in mycoll.aggregate([
            {
                '$match': {'neighbourhood': neighbourhood}
            },
            {
                '$group': {'_id': neighbourhood, 'rental_cost_avg': {'$avg': '$price'}}
            }
        ]):
        print(x)

main()
