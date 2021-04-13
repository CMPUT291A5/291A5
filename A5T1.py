# this code is used to create the sqlite3 database for part 1
# this code is written by Hongyang bai
import csv
import sqlite3

# open YVR_Airbnb_listings_summary.csv copy & all data to our list
csvread_sum = open("YVR_Airbnb_listings_summary.csv", "r", encoding="utf-8")
reader_sum = csv.reader(csvread_sum)

# skip the header & copy it into our sumlist
next(reader_sum)
sumlist = [column for column in reader_sum]

# create database file, set the text factory as string
conn = sqlite3.connect('A5.db')
conn.text_factory = str
c = conn.cursor()

# drop the table before create
c.execute('''DROP TABLE IF EXISTS listings ''')
c.execute('''CREATE TABLE listings (
    id INTEGER,
    name TEXT,
    host_id INTEGER,
    host_name TEXT,
    neighbourhood TEXT,
    room_type TEXT,
    price INTEGER,
    minimum_nights INTEGER,
    availability_365 INTEGER,
    PRIMARY KEY (id)); ''')

# insert data into the .db file
for i in range(len(sumlist)):
    c.execute('''INSERT INTO listings(id, name, 
    host_id, host_name, neighbourhood, room_type, 
    price, minimum_nights, availability_365) 
    VALUES (?,?,?,?,?,?,?,?,?);''', sumlist[i])

# close the connection
conn.commit()
conn.close()

# open YVR_Airbnb_reviews.csv copy & all data to our list
csvread_rev = open("YVR_Airbnb_reviews.csv", "r", encoding="utf-8")
reader_rev = csv.reader(csvread_rev)

# skip the header & copy data into our revlist
next(reader_rev)
revlist = [column for column in reader_rev]

# create database file, set the text factory as string
conn = sqlite3.connect('A5.db')
conn.text_factory = str
c = conn.cursor()

# drop the table before create
c.execute('''DROP TABLE IF EXISTS reviews ''')
c.execute('''CREATE TABLE reviews (
    listing_id INTEGER,
    id INTEGER,
    date TEXT,
    reviewer_id INTEGER,
    reviewer_name TEXT,
    comments TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (listing_id) REFERENCES listings(id));''')

# insert data into the .db file
for i in range(len(revlist)):
    c.execute('''INSERT INTO reviews (listing_id, id,
    date, reviewer_id, reviewer_name, comments)
    VALUES (?,?,?,?,?,?);''', revlist[i])

# close the connection
conn.commit()
conn.close()
