import RPi.GPIO as GPIO
import time
import sqlite3
from datetime import datetime

pir_pin = 18
led_pin = 24

con = sqlite3.connect("pirdb.db")
cursor = con.cursor()

cursor.execute("""
create table if not exists pir_data(
id integer primary key autoincrement,
result text,
created datetime)
""")
print("table created")

con.commit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

print("waiting for pir sensor")


while True :
	motion = GPIO.input(pir_pin)

	if motion :
		print("motion detected")
		GPIO.output(led_pin,GPIO.HIGH)
		cursor.execute(f"insert into pir_data(result,created) values('detected','{datetime.now()}')")
		print("data inserted")
		con.commit()
	else :
		print("motion not detected")
		GPIO.output(led_pin,GPIO.LOW)
	time.sleep(0.5)

cursor.close()
con.close()
