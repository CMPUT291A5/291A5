# 291 A5 Task4 MongoDB
import pymongo


def main():
    print("Task 4 MongoDB")
    # open db
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["A5db"]
    for x in mydb.reviews.aggregate([
            {'$lookup': {'from':"listings", 'localField':"listing_id", 'foreignField': "id", 'as': "listings_docs" }},
            {'$match': {'comments':{'$ne':''}}},{'$sort': {'id':1}},
            {'$limit': 10}, {'$project':{'_id':0,'id':1}}]):
        print(x)

main()
