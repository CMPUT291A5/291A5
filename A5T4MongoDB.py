# 291 A5 Task4 MongoDB
import pymongo


# {'$match': {'$or':{'comments':{'$eq':''},{ '$exists': False } }}},

def main():
    print("Task 4 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    for x in mydb.listings.aggregate([
        {'$lookup': {'from': "reviews", 'localField': "id", 'foreignField': "listing_id", 'as': "reviews_list"}},
        {'$match': {"reviews_list": []}},
        {'$project': {'_id': 0, 'id': 1}},
        {'$sort': {'id': 1}},
        {'$limit': 10}]):
        print(x)


main()

