import RPi.GPIO as IO
import sqlite3
from datetime import datetime
import time

conn = sqlite3.connect("obstacle.db")
cur =conn.cursor()

cur.execute("""
	create table if not exists obstacle_data(id integer primary key autoincrement,status text,date_time text)
 """)
conn.commit()

IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(8,IO.IN)
IO.setup(3,IO.OUT)

while 1 :
	#print(IO.input(8))
	#time.sleep(0.5)
	#if(IO.input(8) == False) :
	if(IO.input(8) == True) :
		print("obstacle detected !! ")
		IO.output(3,True)
		cur.execute("insert into obstacle_data(status,date_time) values (?,?)",("obstacle detected..",datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
		conn.commit()

	else :
		print("obstacle not detected!!")
		IO.output(3,False)
		cur.execute("insert into obstacle_data(status,date_time) values (?,?)",("obstacle not detected..",datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
		conn.commit()
	time.sleep(1)

