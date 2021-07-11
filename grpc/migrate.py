import csv, sqlite3, ciso8601, os
from datetime import datetime

DB_NAME = "measurement.db"

try:
    # To clean up the database
    os.remove(DB_NAME)
except:
    pass

con = sqlite3.connect(DB_NAME) 
# con = sqlite3.connect(':memory:')

cur = con.cursor()
cur.execute("""CREATE TABLE meterusage (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    time TIMESTAMP NOT NULL,
    meter REAL NOT NULL);""") 

with open('meterusage.1625582172.csv','r') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(datetime.timestamp(ciso8601.parse_datetime(i['time'])), i['meterusage']) for i in dr]

print(to_db)

cur.executemany("INSERT INTO meterusage (time, meter) VALUES (?, ?);", to_db)
con.commit()
con.close()
