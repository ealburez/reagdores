#!/usr/bin/python

import RPi.GPIO as GPIO
import sys, time

#------------------------------
#	varaibles
#------------------------------

outPin = [11,13,15]
try:
	sleepTime = int(sys.argv[1])*60
except:
	sleepTime = 0

#------------------------------
#	Funciones
#------------------------------

def setRegador (idTag,waitTime):
	print "encendiendo",idTag, waitTime
	GPIO.output(idTag, GPIO.HIGH) #Turn on
	time.sleep(waitTime)	#wait until shutting sprinkler off
	GPIO.output(idTag, GPIO.LOW) #Turn off



#------------------------------
#	Program
#------------------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#---Apagar todos los regadores---
for i in range(len(outPin)):
	GPIO.setup(outPin[i],GPIO.OUT)	#Define as output
	GPIO.output(outPin[i], GPIO.LOW) #Turn off
	print "apaga" , outPin[i]

#---Prender los regadores en secuencia

if len(sys.argv)==2:
	for i in range(len(outPin)):
		setRegador(outPin[i],sleepTime)

#---Prender un regador
elif len(sys.argv)==4:
	pin=outPin[sys.argv[3]]
	setRegador(pin,sleepTime)
	#logica para programar un regador
