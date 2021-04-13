# 291 A5 task 2
# Written by Bowen Xiao
from pymongo import MongoClient
import csv


def read_reviews():
    # read reviews
    filename = 'YVR_Airbnb_reviews.csv'
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        reviews_list = [column for column in reader]
    f.close()
    return reviews_list


def read_listings():
    # read listings
    filename = 'YVR_Airbnb_listings_summary.csv'
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        listings_list = [column for column in reader]
    f.close()
    return listings_list


def create_db(review_list, listing_list):
    # create A5db
    c = MongoClient()
    db = c.A5db

    for row in review_list:
        # create reviews table
        collection = db.reviews
        item = {
            "listing_id": int(row[0]),
            "id": int(row[1]),
            "date": row[2],
            "reviewer_id": (row[3]),
            "reviewer_name": row[4],
            "comments": row[5]
        }
        collection.insert_one(item)

    for row in listing_list:
        # create listings table
        collection = db.listings
        item = {
            "id": int(row[0]),
            "name": row[1],
            "host_id": int(row[2]),
            "host_name": row[3],
            "neighbourhood": row[4],
            "room_type": row[5],
            "price": int(row[6]),
            "minimum_nights": int(row[7]),
            "availability_365": int(row[8])
        }
        collection.insert_one(item)


def main():
    review_list = read_reviews()
    print("Finish read data from reviews")
    listing_list = read_listings()
    print("Finish read data from listings")
    create_db(review_list, listing_list)
    print("done")


main()
