#!/usr/bin/python

#######################################################################
#
# File:		./main.py
#
# Date:		02.06.2015 
# Update:	
#
# Auth:		Henryk Hellebrand
#
# Descr:	autotests
#
#######################################################################

import sys
import os
import subprocess
sys.path.append('/home/testing/Ta/libs')
sys.path.append('/home/testing/Ta/include')
sys.path.append('/home/testing/Ta/class')
import lib_oid
import class_snmp
import class_menu
import class_log
import datetime
import time 
import wanip
from numpy import*
switch = "192.168.0.20"
path = "/home/testing/Ta/results/"


def box_cm(ip,pat):
    name = pat+"/NMAP_LAN_CM_"+ip
    aa = len(ip)
    if aa > 15:
	_nmap6(name,ip)    
    else:
	_nmap4(name,ip)    
    

def _nmap4(name,ip):
    comm='sudo nmap -sS -sU -T4 -A -v -PE -PS22,25,80 -PA21,23,80,3389 -oX '+name+'.xml '+ip+' &'    
    print comm
    #proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    #output=proc.communicate()[0]			

def _nmap6(name,ip):
    comm='sudo nmap -sS -sU -T4 -A -v -6 -PE -PS22,25,80 -PA21,23,80,3389 -oX '+name+'.xml '+ip+' &'    
    print comm
    #proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    #output=proc.communicate()[0]			

def closeports():
    for n in range(3,25):
	oi = "IF-MIB::ifAdminStatus."+str(n)
        print oi
        #class_snmp._snmpset(switch,oi,"integer","2")
    

################### main ###########################
tim = datetime.datetime.now().strftime("%d%m%Y")
pat = path+"NmapResults_"+tim
if not os.path.exists(pat):
    os.makedirs(pat)
else:
    print "exist"
closeports()

f = open('/home/testing/Ta/cmlist.txt')
for line in iter(f):    
    aa = line
    aa = aa.rstrip("\r\n")
    bb = aa.split('=')
    if bb[0] == "port":
	port = bb[1]
	oid = "IF-MIB::ifAdminStatus."+port
	port2 = int(port) - 1
	port2 = str(port2)
	oid2 = "IF-MIB::ifAdminStatus."+port2

	class_snmp._snmpset(switch,oid,"integer","1")
	class_snmp._snmpset(switch,oid2,"integer","2")
    box_cm(aa,pat)
f.close()
closeports()
