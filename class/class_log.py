#!/usr/bin/python

import io
import sys
import os
import datetime
sys.path.append('/home/testing/Ta/class')
sys.path.append('/home/testing/Ta/libs')


name = {'name':''}

tim = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
file_w = open("logs/"+name['name']+"_"+ tim +".log", "w+")
#file_csv = open("logs/SIGNAL" + tim + ".csv", "w+")
#file_csv.write("Date;Time;DsPower;UsPower;DsSNR;Ping;FEC unerror;FEC corrected;FEC uncorrected \n")

def dajmi():
    return file_w


def create_file(data):
    file_w.write(data)
    

def close_file():
    file_w.close()


#def create_csv(row):
#    file_csv.write(row)
    
def extra_4491(data):
    file_w2 = open("/home/testing/Ta/logs/_4491CMSNMP"+ tim +".log", "w+")
    file_w2.write(data)
    file_w2.close()