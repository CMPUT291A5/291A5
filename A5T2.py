'''
291 A5 task2 
'''

import pymongo
import csv


def analysis_sum(file):
    csv_file = csv.reader(file)   # convert file to csv.reader object
    head_row = next(csv_file)   # remove first line(title)
    for row in csv_file:
        history_item = dict()
        history_item["id"] = row[0]
        history_item["name"] = row[1]
        history_item["host_id"] = row[2]
        history_item["host_name"] = row[3]
        history_item["neighbourhood"] = row[4]
        history_item["room_type"] = row[5]
        history_item["price"] = row[6]
        history_item["minimum_nights"] = row[7]
        history_item["availability_365"] = row[8]
        collection1.insert(history_item)

def analysis_review(file):
    csv_file = csv.reader(file)  # convert file to csv.reader object
    head_row = next(csv_file)  # remove first line(title)
    for row in csv_file:
        history_item = dict()
        history_item["listing_id"] = row[0]
        history_item["id"] = row[1]
        history_item["date"] = row[2]
        history_item["reviewer_id"] = row[3]
        history_item["reviewer_name"] = row[4]
        history_item["comments"] = row[5]
        collection2.insert(history_item)


if __name__ == '__main__':
    # build connection
    host = 'localhost'
    port = 27017
    client = pymongo.MongoClient(host=host, port=port)
    # connect dataBase
    db1 = client['A5db']  # choose repository
    collection1 = db1['listings']  # choose table
    # get data
    csv_sum = open('YVR_Airbnb_listings_summary.csv', "r")
    analysis_sum(csv_sum)

    db2 = client['A5db']  # choose repository
    collection2 = db2['reviews']  # choose table
    csv_review = open("YVR_Airbnb_reviews.csv","r")
    analysis_review(csv_review)
