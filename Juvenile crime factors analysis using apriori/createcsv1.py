import sys
import csv
import os
import sqlite3
con = sqlite3.connect('crime1')

cur = con.cursor()
cur.execute('SELECT * FROM factors;')
rows = cur.fetchall()
fp = open('factors1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('factors1.csv file successfully created')
con.commit()