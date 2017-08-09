#!/usr/bin/python

#######################################################################
#
# File:		./main.py
#
# Date:		27.02.2015 
# Update:	
#
# Auth:		Henryk Hellebrand
#
# Descr:	multitest script
#
#######################################################################

import sys
import os
import subprocess
sys.path.append('libs')
sys.path.append('include')
sys.path.append('class')
import lib_oid
import class_snmp
import class_menu
import class_log
import datetime

snmp = class_snmp.snmp()
tftp = "83.169.189.65"
tot = len(sys.argv)

def read_params(ip):
	oisw = lib_oid._sysdescr
	oido = lib_oid._oid
	oidv = lib_oid._vendor
	oidm = lib_oid._model
	class_menu.par['oid'] = class_snmp._snmpget2(ip,oido)
	class_menu.par['vendor'] = class_snmp._snmpget2(ip,oidv)
        class_menu.par['vendor'] = class_menu.par['vendor'].replace('"','')
        class_menu.par['vendor'] = class_menu.par['vendor'].replace('-','')
        class_menu.par['vendor'] = class_menu.par['vendor'].replace(' ','')
        class_menu.par['vendor'] = class_menu.par['vendor'].replace(',','')
        class_menu.par['vendor'] = class_menu.par['vendor'].replace('.','')
        class_menu.par['vendor'] = class_menu.par['vendor'].rstrip("\r\n")
	class_log.create_file("\n#\t\t Vendor : "+class_menu.par['vendor']+" ")
	class_menu.par['model'] = class_snmp._snmpget2(ip,oidm)
	class_menu.par['model'] = class_menu.par['model'].replace('"','')
	class_menu.par['model'] = class_menu.par['model'].replace('-','')
    	class_menu.par['model'] = class_menu.par['model'].replace('.','')
	class_menu.par['model'] = class_menu.par['model'].rstrip("\r\n")
	class_log.create_file("\n#\t\t Model : "+class_menu.par['model']+" ")
	class_menu.par['tftpd'] = tftp
	class_menu.par['swtransportprotocol'] = "1"
	class_menu.par['swserveraddresstype'] = "1"
	sw = class_snmp._snmpget2(ip,oisw)
	si = sw.split('SW_REV:')
	sii = si[1].split(';')
	class_menu.par['mac'] = sii[0]
	class_log.create_file("\n#\t\t SW : "+class_menu.par['mac']+" \n#")
	class_log.create_file("#"*80)
	#print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddress,"x",par['Test SW 01'])

def _help():
    print "Usage:"
    print "\t./main.py [options] "
    print "\t./main.py ip_address"

def ping(ip):
    comm='ping -c 1 ' + ip
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]		
    #out = output.split('/')	
    return output

if tot < 2:
    _help()

else:
    tim = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    lle = len(sys.argv[1])
    if lle > 15:
	class_menu.par['ipv'] = "6"
    else: 
	class_menu.par['ipv'] = "4"

    if sys.argv[2:]:
	class_menu.par['tc'] = str(sys.argv[2])		
    else:
	class_menu.par['tc'] = "log"		

    class_log.create_file("#\n#\t\t Start Test :" +tim)
    class_menu.par['ip'] = str(sys.argv[1])    
    ip = str(sys.argv[1])
    aaa = ping(ip)
    if ('ttl=' in aaa):
	print "ok"
	read_params(ip)    
    else:
	print "noo"    

    class_menu.main_menu()    
    #print lib_oid.EvId

