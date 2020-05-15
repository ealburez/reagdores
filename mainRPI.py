#!/usr/bin/python

import csv

dirFiles="/var/www/html/"


confFile=dirFiles + "regadores.conf"
command = dirFiles + "water.py" 

with open(confFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #check for wrong data
    for row in csv_reader:
        for x in range (2,4): # check the start and stop time
            if not row[x].replace(":","").isdigit():
                row[x]="00:00"
                
        if not row[4].isdigit(): # check duration
            row[4]="1"
        print(row)        
    #-------------------
    # construct crontab
    #-------------------
    
    header = "# m h  dom mon dow   command\nPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games\n"
    body="" 
    for row in csv_reader: 
        startHour=row[2].split(":")
        body += startHour[1] + " " +startHour[0] + " * * * " + command +"\n"
            
    
