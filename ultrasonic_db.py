import RPi.GPIO as GPIO
import time 
import sqlite3

TRIG  = 21
ECHO = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

conn = sqlite3.connect("ultrasonic_sensor.db")
cursor = conn.cursor()

cursor.execute("""
	create table if not exists ultrasonic_data(id integer primary key AUTOINCREMENT,
	distance real,
	timestamp datetime default current_timestamp)
""")

conn.commit()
try:
	while True:
		GPIO.output(TRIG,False)
		time.sleep(0.2)
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		GPIO.output(TRIG,False)
		while GPIO.input(ECHO)==0:
			pulse_start=time.time()
		while GPIO.input(ECHO)==1:
			pulse_end=time.time()
		pulse_duration=pulse_end-pulse_start
		distance=pulse_duration*17150
		distance=round(distance,2)
		print("distance:",distance,"cm")
		cursor.execute("insert into ultrasonic_data(distance) values(?)", (distance,))
		conn.commit()
		time.sleep(2)
except KeyboardInterrrupt:
	print("Program Stopped")
finally:
	GPIO.cleanup()
	conn.close()		

