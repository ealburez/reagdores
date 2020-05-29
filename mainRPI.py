#!/usr/bin/python

import csv
from crontab import CronTab


#system varaibles
usuario="www-data"

#directory variables
dirFiles="/var/www/html/"
confFile=dirFiles + "regadores.conf"
crontabFile = dirFiles + "schedule.crontab"
commandFile = dirFiles + "water.py"
comando = "python "+commandFile 

#Initialize Crontab
my_cron = CronTab(user=usuario)
my_cron.remove_all()
job=[]
i = 0

#header = "# m h  dom mon dow   command\nPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games\n"
#body=""

with open(confFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #check for wrong data
    for row in csv_reader:
        for x in range (2,4): # check the start and stop time
            if not row[x].replace(":","").isdigit():
                row[x]="00:00"
                row[1]=""       #deactivate the sprinkler
                
        if not row[4].isdigit(): # check duration
            row[4]="1"
        print(row)
        #-------------------
        # construct crontab body
        #-------------------
        if row[1]=="1": #checks if  the sprinkler is enabled
            startHour=row[2].split(":")
            job.append(my_cron.new(command=comando + " " + row[0] + " " + row[4] , comment = row[0]))
            body = startHour[1] + " " +startHour[0] + " * * *"
            job[i].setall(body)
            i += 1       #incrementar el contador si se agrego un job
        
    #----------------------
    # guardar en crontab
    #----------------------
    
    my_cron.write()
    
            
    
