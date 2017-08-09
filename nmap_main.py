#!/usr/bin/python

#######################################################################
#
# File:		./nmap_main.py
#
# Date:		06.03.2015 
# Update:	
#
# Auth:		Henryk Hellebrand
#
# Descr:	nmap in multi thread   
#
#######################################################################

import sys
import os
import time
import subprocess

from thread import start_new_thread, allocate_lock

class c:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   B = '\033[1m'
   U = '\033[4m'
   END = '\033[0m'

num_threads = 0
thread_started = False
lock = allocate_lock()
#q='.'

def _nmap(aaa):
    global num_threads, thread_started
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()
    
    comm='sudo nmap -sS -sU -T4 -A -v -PE -PS22,25,80 -PA21,23,80,3389 -oX tset-wo-RF_tcp_udp_LAN_to_'+aaa+'.xml '+aaa    
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			

#	  sudo nmap -sS -sU -T4 -A -v -6 -PE -PS22,25,80 -PA21,23,80,3389 -oX

    lock.acquire()
    num_threads -= 1
    lock.release()

tot = len(sys.argv)

def _start(tot):
    q = '.'
    for a in range(1,tot):
	ip = str(sys.argv[a])
        start_new_thread(_nmap,(ip,))

    while not thread_started:
        pass
    while num_threads > 0:
        time.sleep(1)
        os.system('clear')
        ss = str(num_threads)
        e = 'Port Scanning: ('+ss+ ') Cable modems['
        r = ']'	
        q += '.'
        w = q.count('.')
        if w == 30:
		q = '.'
        print c.B+e+q+r+c.END
        pass

if tot < 2:
    print "Usage:"
    print "\t./nmap_main.py [options] "
    print "\t./nmap_main.py ip_address ipaddress_next"
else:
    _start(tot)
