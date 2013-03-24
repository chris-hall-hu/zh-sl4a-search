import os
import sqlite3
from time import sleep

path = os.path.abspath(__file__)
dname = os.path.dirname(path)

dbpath = dname + '/Chinese.sqlite'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

file = open(dname + '/freq.txt')

for line in iter(file):
  print line
  words = line.split()
  if len(words) > 2:
    print words[0] + words[1] + " " + words[2]
    
    conn.execute("update chinese set freq = ? where Simplified = ?",(words[1],words[2].decode('utf-8'))) 

conn.commit()
conn.close() 
file.close()
