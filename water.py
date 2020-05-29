#!/usr/bin/python

import RPi.GPIO as GPIO
import sys, time

#------------------------------
#	varaibles
#------------------------------

outPin = [11,15,17]
try:
	sleepTime = argv[1]*60
except:
	pass

#------------------------------
#	Funciones
#------------------------------

def setRegador (idTag,waitTime):
	print "encendiendo",idTag, waitTime
	GPIO.output(idTag, GPIO.HIGH) #Turn on
	time.sleep(waitTime)	#wait until shutting sprinkler off
	GPIO.output(led, GPIO.LOW) #Turn off



#------------------------------
#	Program
#------------------------------
GPIO.setmode(GPIO.BOARD)

#---Apagar todos los regadores---
for i in range(len(outPin)):
	GPIO.setup(i,GPIO.OUT)	#Define as output
	GPIO.output(i, GPIO.LOW) #Turn off
	print "apaga" , i

#---Prender los regadores en secuencia

if len(sys.argv)==2:
	for i in range(len(outPin)):
		setRegador(outPin[i],sleepTime)

#---Prender un regador
elif len(sys.argv)==4:
	setRegador(argv[3],sleepTime)
	#logica para programar un regador
