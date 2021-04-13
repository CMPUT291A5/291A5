from pymongo import MongoClient
import sys


print("Task 9")
# open db
c = MongoClient()
db = c.A5db
collection = db.reviews

# get the input from command line
if len(sys.argv) > 1:
    myinput = sys.argv[1]
else:
    myinput = (input("Please enter keyword(s): "))

#replace , for using, create index for $text
myinput = myinput.replace(",", ' ')
collection.create_index([("comments",'text')])

#find the top 3 reviews and order them by score
lists = collection.find(
    {"$text": {"$search": myinput}},
    {"score": {"$meta": "textScore"}},
).limit(3)
lists.sort([('score', {'$meta': 'textScore'})])



for i in lists:
    print(i, '\n')
