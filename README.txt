In this A5.tgz file there are 11 A5T*.py files and 1 README text
ALL WORK ARE DONE BY Hongyang Bai, Xinyuan Zhao, Bowen Xiao
CCID: hb2, xinyuan7, bxiao

A5T1.py A5.db 
This file is used to create the sqlite3 A5.db, use command "python3 A5T1.py" to execute it

A5T2.py A5db 
This file is used to create the mongodb A5db, use command "python3 A5T2.py" to execute it

A5T3SQLite.py and A5T3MongoDB.py
Both of them runs in same way: "Python3 A5T3***.py" to execute it.
It will return the number of rentals the host holds, the host ID, and their name 
we select all host_id and group by host_id, count the number of rentals and order by host ID 
(NEVER ORDERED BY NUMBER OF RENTALS)


A5T4SQLite.py and A5T4MongoDB.py
Both of them runs in same way: "Python3 A5T4***.py" to execute it
It will return the listing_id which has never received a review
we select the listing_id WITH comment first, then select id which NOT IN the previous listing_id to get the answer
(top 10 is ordered by listing_id)

A5T5SQLite.py and A5T5MongoDB.py
Both of them runs in same way: "Python3 A5T5***.py 'NEIGHBOURHOOD_NAME' " to execute the average price of given neighbourhood
EX: Python3 A5T5***.py Downtown 
we select the average price which neighbourhood = 'given neighbourhood name' and type changed as integer
It will return the average price per night of the given neighbourhood

A5T8SQLite.py and A5T8MongoDB.py
Both of them runs in same way: "Python3 A5T8***.py 'listing_id' " to execute the most recent commant this id received. 
EX: Python3 A5T8***.py 10080
we select the data from two tables, which condition is that group by listing_id and order commant by date DESC limit of commant is 1
It will return the host_name, rental_price and the most recent review for that listing.

A5T9MongoDB.py
using command line to run "Python3 A5T9***.py 'keyword1','keyword2' "
EX: Python3 A5T9***.py nice, good, best
PLEASE SPLIT EACH KEYWORD BY ','
We use $text & $search to find the commands which keyword is included, and then group by listing_id to figure out the top 3
It will return the top 3 rentals which commants have the most keywords. 


