#!/usr/bin/python

import csv
import csv
import csv

with open('regadores.conf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for x in range (2,3)
        if !row[x].replace(":","").isdigit()
            row[x]="00:00"
            
        print(row)
