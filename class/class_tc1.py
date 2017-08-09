import curses                                                                
from curses import panel                                                     
import os
import re
import sys
import time
import datetime
import subprocess
import operator
import binascii
import socket
sys.path.append('/home/testing/Ta/libs')
import lib_menu
import lib_oid
import lib_sw
import class_log
import class_snmp
import class_cmts
import class_menu

snmp = class_snmp.snmp()
cmts = class_cmts.cmts()

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


def _logic(info,value):
    out = value.rstrip("\r\n")
    ans = ""
    if out == "1":
	ans = " : UP"
	print info+c.B+c.GREEN+ans+c.END
    else:
	ans = " : DOWN"
	print info+c.B+c.RED+ans+c.END


def cm_info(par):
	class_log.create_file("\n#\n#\t\t Device Parts Status Router/CM/MTA/ETH-CPE: \n#\n")
	#router
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_Router_admin)
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_Router_oper)
	_router_adm = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_Router_admin)
	_logic("Router Admin Status: ",_router_adm)
	_router_oper = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_Router_oper)
	_logic("Router Operational Status:",_router_oper)
	#cm
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_CM_admin)
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_CM_oper)
	_cm_adm = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_CM_admin)
	_logic("CM Admin Status: ",_cm_adm)
	_cm_oper = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_CM_oper)
	_logic("CM Operational Status: ",_cm_oper)
	#mta
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_MTA_admin)
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_MTA_oper)
	_mta_adm = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_MTA_admin)
	_logic("MTA Admin Status: ",_mta_adm)
	_mta_oper = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_MTA_oper)
	_logic("MTA Operational Status: ",_mta_oper)
	#router
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_ETH_CPE_admin)
	class_snmp._snmpwalk(par['ip'],lib_oid.STAT_ETH_CPE_oper)
	_cpe_adm = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_ETH_CPE_admin)
	_logic("ETH CPE Admin Status: ",_cpe_adm)
	_cpe_oper = class_snmp._snmpwalk2(par['ip'],lib_oid.STAT_ETH_CPE_oper)
	_logic("ETH CPE Operational Status: ",_cpe_oper)
    	#####################################################    

########################### SPEED 

def iphex(iip):
    iip = binascii.hexlify(socket.inet_aton(iip))
    return iip

def speed(par):
    class_log.create_file("\n#\n#\t\t IPERF SPEED TEST: \n#\n")
    if par['model'] == "CH6640E":
	var = ""
	class_menu.speed['type'] = '1'
	class_menu.speed['ip'] = '10.9.4.40'
	class_menu.speed['port'] = '5031'
	class_menu.speed['interval'] = '20'
	class_menu.speed['packsize'] = '1400'
	class_menu.speed['time'] = '30'
	iperf_server_type = "1.3.6.1.4.1.35604.1.19.61.3.1.0"
	iperf_server_ip = "1.3.6.1.4.1.35604.1.19.61.3.2.0"
	iperf_port = "1.3.6.1.4.1.35604.1.19.61.3.3.0"
	iperf_packet_size = "1.3.6.1.4.1.35604.1.19.61.3.4.0"
	time_test = "1.3.6.1.4.1.35604.1.19.61.3.5.0"
	reset_counter = "1.3.6.1.4.1.35604.1.19.61.3.6.0"
	re = "1.3.6.1.4.1.35604.1.19.61.3.9.0"
	alle = "1.3.6.1.4.1.35604.1.19.61.3"
	typ = class_snmp._snmpwalk4(par['ip'],iperf_server_ip)	
	if ('IpAddress' in typ):
	    var = "a"
	else:
	    var = "x"
	    class_menu.speed['ip'] = iphex(class_menu.speed['ip'])
	
	print class_snmp._snmpset(class_menu.par['ip'],iperf_server_type,"i",class_menu.speed['type'])
	print class_snmp._snmpset(class_menu.par['ip'],iperf_server_ip,var,class_menu.speed['ip'])
	print class_snmp._snmpset(class_menu.par['ip'],iperf_port,"u",class_menu.speed['port'])
	print class_snmp._snmpset(class_menu.par['ip'],iperf_packet_size,"u",class_menu.speed['packsize'])
	print class_snmp._snmpset(class_menu.par['ip'],time_test,"i",class_menu.speed['interval'])
	print class_snmp._snmpset(class_menu.par['ip'],reset_counter,"i","1")
	com = "iperf -u -c " + class_menu.par['ip'] + " -p "+class_menu.speed['port']+" -t "+class_menu.speed['interval']+" -l "+class_menu.speed['packsize']+ " -b 450.0M"	
        proc=subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, )
        output=proc.communicate()[0]			
	print output
	print time.sleep(5)
	res = class_snmp._snmpwalk2(par['ip'],re)	
	print "*"*80
	res = res.rstrip("\r\n")
	print "\n\n Result : " +c.B +c.RED+ res + " bytes/s" +c.END+ "\n\n"
	print "*"*80
	alll = class_snmp._snmpwalk(par['ip'],alle)	
	print alll
    #if par['model'] == "CHE1":
    #if par['model'] == "CHE2":
    #if par['model'] == "CHE3":
    #if par['model'] == "CHE4":

def check_log(par):
	if class_menu.par['model'] == "TC7200K":
	    box_CM_MAC = "1.3.6.1.2.1.2.2.2.1.6.2"
	    box_IF = "1.3.6.1.2.1.4.22.1.1"
	    box_MAC_IF = "1.3.6.1.2.1.4.22.1.2"
	    box_IP_IF = "1.3.6.1.2.1.4.22.1.3"
	    box_cm_mac1  = "1.3.6.1.2.1.4.22.1.3.1"
	    box_cm_ip1 = "1.3.6.1.2.1.4.22.1.2.1"

	    mta_part = "1.3.6.1.4.1"


	    aaa = class_snmp._snmpwalk2(par['ip'],box_IP_IF)
	    aaa = aaa.rstrip("\r\n")
	    aaa = aaa.split("\n")
	    siz = len(aaa)
	    siz -= 1
	    mtaip = aaa[siz]
	    print mtaip
	    
	    class_log.create_file("\n#\n#\t\t CM Informations: \n#\n")
	    print class_snmp._snmpwalk_(par['ip'],box_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_MAC_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_IP_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_cm_mac1)
	    print class_snmp._snmpwalk_(par['ip'],box_cm_ip1)

	    class_log.create_file("\n#\n#\t\t MTA LOGS: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,mta_part)


	    


	if class_menu.par['model'] == "cmp":
    	    box_CM_MAC = "1.3.6.1.2.1.2.2.2.1.6.2"
	    box_IF = "1.3.6.1.2.1.4.22.1.1"
	    box_MAC_IF = "1.3.6.1.2.1.4.22.1.2"
	    box_IP_IF = "1.3.6.1.2.1.4.22.1.3"
	    box_cm_mac1  = "1.3.6.1.2.1.4.22.1.3.1"
	    box_cm_ip1 = "1.3.6.1.2.1.4.22.1.2.1"

	    mta_country = "1.3.6.1.4.1.35604.1.200.9.12.0"
	    mta_callhistory = "1.3.6.1.4.1.35604.1.200.17.1.1.2.1"
	    mta_tone_ncs = "1.3.6.1.4.1.7432.2.1.1.32"
	    mta_tone_ncs2 = "1.3.6.1.4.1.7432.2.1.1.33"
	    mta_tone_pc20 = "1.3.6.1.4.1.35604.1.200.18.12.1"
	    mta_tone2_pc20 = "1.3.6.1.4.1.35604.1.200.18.13.1"

	    aaa = class_snmp._snmpwalk2(par['ip'],box_IP_IF)
	    aaa = aaa.rstrip("\r\n")
	    aaa = aaa.split("\n")
	    mtaip = aaa[3]

	    class_log.create_file("\n#\n#\t\t CM Informations: \n#\n")
	    print class_snmp._snmpwalk_(par['ip'],box_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_MAC_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_IP_IF)
	    print class_snmp._snmpwalk_(par['ip'],box_cm_mac1)
	    print class_snmp._snmpwalk_(par['ip'],box_cm_ip1)

	    class_log.create_file("\n#\n#\t\t MTA COUNTRY CODE: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,mta_country)
	    class_log.create_file("\n#\n#\t\t MTA INFO: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.2.54")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.9.2")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.13.1.7")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.18.1")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.18.2")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.35604.1.200.18.3")
	    class_log.create_file("\n#\n#\t\t MTA 4491: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,"1.3.6.1.4.1.4491")
	    class_log.create_file("\n#\n#\t\t MTA CALL HISTORY: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,mta_callhistory)
	    class_log.create_file("\n#\n#\t\t MTA NCS: \n#\n")
	    print class_snmp._snmpwalk_(mtaip,mta_tone_ncs)
	    print class_snmp._snmpwalk_(mtaip,mta_tone_ncs2)
	    class_log.create_file("\n#\n#\t\t MTA PC20: \n#\n")
    	    print class_snmp._snmpwalk_(mtaip,mta_tone_pc20)
	    print class_snmp._snmpwalk_(mtaip,mta_tone2_pc20)

