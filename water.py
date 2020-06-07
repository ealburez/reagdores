#!/usr/bin/python

import RPi.GPIO as GPIO
import sys, time, datetime,getpass, psutil

"""
can be called with the following argmunets

water.py ---> turns off all the sprinkler
water.py time(minutes) ---> turns all sprinklers on in sequence for the defined amount of time
water.py time(minutes) sprinklerID ---> turns the defined sprinkler for the defined time

"""


#------------------------------
#	varaibles
#------------------------------

outPin = [11,13,15] #Pins based onboard layout
try:
	sleepTime = float(sys.argv[1])*60
except:
	sleepTime = 0
logFile = "/var/www/html/riego.log"


#------------------------------
#	Funciones
#------------------------------

def setRegador (idTag,waitTime):
	writeLog("encendiendo",idTag, waitTime)
	GPIO.output(idTag, GPIO.HIGH) #Turn on
	time.sleep(waitTime)	#wait until shutting sprinkler off
	GPIO.output(idTag, GPIO.LOW) #Turn off
	writeLog("apagando",idTag)
"""
log event
"""
def writeLog(*kwargs):
	f = open(logFile, "a")
	logOut=str(datetime.datetime.now().strftime("%x %X")) + " "
	for arg in kwargs:
		logOut += str(arg) + " "
	logOut += "\n"
	f.write(logOut)
	f.close()

#------------------------------
#	Program
#------------------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Terminar cualquier proceso activo
for proc in psutil.process_iter(['pid','cmdline']):
	if 'water.py' in proc.cmdline() and proc.info['cmdline'][2] != '0':
		proc.kill() 
		print(proc.pid, proc.cmdline())

#---Apagar todos los regadores---
writeLog("----apagando todos----",len (sys.argv), getpass.getuser())
for i in range(len(outPin)):
	GPIO.setup(outPin[i],GPIO.OUT)	#Define as output
	GPIO.output(outPin[i], GPIO.LOW) #Turn off

#---Prender los regadores en secuencia

if len(sys.argv)==2:
	#Si el tiempo esta en cero no salir del programa
	if sleepTime==0:
		writeLog("---shut off command---")
		sys.exit(0)
	#Si hay tiempo prender por el tiempo especificado
	for i in range(len(outPin)):
		setRegador(outPin[i],sleepTime)

#---Prender un regador si es llamado con 2 parametros
elif len(sys.argv)==3:
	pin=outPin[int(sys.argv[2])]
	setRegador(pin,sleepTime)
	#logica para programar un regador

