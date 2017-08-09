#import curses                                                                
#from curses import panel                                                     
import os
import re
import sys
import time
import datetime
import subprocess
import operator
sys.path.append('/home/testing/Ta/libs')
import lib_menu
import lib_oid
import lib_sw
import class_log
import class_snmp
import class_cmts
#import class_Ta1 

snmp = class_snmp.snmp()
cmts = class_cmts.cmts()
cmtsssh = class_cmts.cmts_ssh()

par = {'ip':'','ipv':'','mac':'','dur':'','tftpd':'','swtransportprotocol':'','swserveraddresstype':'','Test SW 01':'','Test SW 02':'',
	'oid':'','vendor':'','model':'','Ta':''}

PreConditions = {1:'zzz'}
DHCPcriteria = {1:'xxx'}
SNMPOIDafterPROV = {
	1:'2.3.1.1 ifTable IF-MIB (Docsis - 2.0 and 3.0)',
	2:'2.3.1.2 DOCS-CABLE-DEVICE-MIB (Docsis - 2.0 and 3.0)',
	3:'2.3.1.3 ifTable IF-MIB (Docsis 2.0)',
	4:'2.3.1.4 DOCS-IF3-MIB (Docsis 3.0)'
}

GUIWanLan = {1:'eee'}
FTPIperf = {1:'qqq'} 
SWupDOWN = {1:'qwe'}
Tarif = {1:'ewq'}
Functional = {1:'asd'}
SecondLineOption = {1:'te'}
HomespotGUI = {1:'tretw'}
CMMTAIPsix = {1:'frewfe'}
SWupDOWNconv = {
	1:'not implemented',
	2:'2.12.2 The firmware information in the SNMP MIB SysDescr.0 MUST be displayes as'
}

RemoteManagement = {1:'bb'}
FactoryDefaults = {1:'aaa'}

speed = {
	    'type':'',
	    'ip':'',
	    'port':'',
	    'interval':'',
	    'packsize':'',
	    'time':''
	}

Provisioning = {
	1:'aaa',
	2:'bb',
	3:'ccc'}


cmtest = {
	    1:'System Description',
	    2:'Cable Modem Status',
	    3:'Cable Modem Event Log',	    
	    4:'Cable Modem Part Information',
	    5:'Verify the DOCSIS Event Logs',
	    6:'Verify HOME SPOT',
	    7:'macro 1',	    
	    8:'Reboot',
	    9:'cm sw update test01',
	    10:'cm sw update test02',
	    11:'Signal Test'}

testset = {
	    1:'IP address',
	    2:'MAC address',
	    3:'Test duration',
	    4:'TFTPD address',
	    5:'SWTransportProtocol'
	  }

boxtest = {
	    1:'CM information',
	    2:'CM,MTA,CPE ip'
	    }

mv = { 'old':'',
	'new':''
	}

cmtstest = {1:'scm',
	    2:'cpe',
	    3:'cpe ipv6',
	    4:'cpe qos',
	    5:'cpe details'}

Ta1 = {
	    1:'2.1.1',2:'2.5.1',3:'2.5.2',4:'2.6.1.1',5:'3.2.1.1~4',6:''
	    
	    }

def pause():
    try:
	input("Press Enter to continue...")
    except SyntaxError:
        pass

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

def check(aaa):
    if "CVE30360" == par['model']:
	_function2(lib_sw.CVE30360,aaa)	
    if "CH6640E" == par['model']:	
	_function2(lib_sw.CH6640E,aaa)
    if "6490" == par['model']:	
	_function2(lib_sw.A6490,aaa)
    if "Ta7200K" == par['model']:	
	_function2(lib_sw.Ta7200K,aaa)



def conv():
    baa = class_log.dajmi()
    ba1 = str(baa)
    ba1 = ba1.split("'")
    ba2 = ba1[1].split('/')
    nn = str(par['Ta'])
    nn1 = str(ba2[1])
    nam = nn+nn1
    mv['old'] = nn1
    mv['new'] = nam

###########################################################
def main_menu():
    repeat = "yes"
    while repeat == "yes":
	os.system('clear')
	lib_menu._logo(par)
        lib_menu._main(lib_menu.main)
	dice = raw_input('select:')
	if dice == "q": ####### quit
	    class_log.close_file()	    
	    #os.mkdir ("reports/"+par['Ta'])
	    newname = conv()
	    os.rename("logs/"+mv['old'],"logs/"+mv['new'])

	    print "Done"
	    repeat = "no"
	if dice == "2": ###### cable modem	    
	    _function(Provisioning)
	    repeat = "no"
	if dice == "1": ###### cmts
	    _function(cmtstest)
	    repeat = "no"
	if dice == "3": ###### setting test
	    _function(SNMPOIDafterPROV)
	    repeat = "no"
	if dice == "4": ###### setting test
	    _function(testset)
	    repeat = "no"
	if dice == "5": ###### setting
	    check('ts1')
	    repeat = "no"
	if dice == "6": ###### setting
	    check('ts2')
	    repeat = "no"
	if dice == "7": ###### setting
	    check('fs1')
	    repeat = "no"
	if dice == "8": ###### setting
	    check('fs2')
	    repeat = "no"
	if dice == "9": ###### setting
	    _function(Ta1)
	    repeat = "no"
	
	if dice == "12": ###### setting
	    _function(SWupDOWNconv)
	    repeat = "no"
###########################################################		


	    		
def _function(tab):
    print tab
    repeat = "yes"
    while repeat == "yes":
	os.system('clear')
	lib_menu._logo(par)
        lib_menu.draft(tab)	
	dic = raw_input('select:')
	if dic == "q":
	    main_menu()
	    repeat = "no"
	else:		 
	    for i in tab:	
		w = str(i)
		
		if dic == w:
		    _exec(tab[i])				
		    pause()


def _function2(tab,aaa):
    #print tab
    repeat = "yes"
    while repeat == "yes":
	os.system('clear')
	lib_menu._logo(par)
        lib_menu.draft(tab)
	dic = raw_input('select:')	
	if dic == "q":
	    main_menu()
	    repeat = "no"
	else:		 
	    for i in tab:
		w = str(i)	    	
		if dic == w:
		    ss = tab[i]
		    _exec2(ss,aaa)		    		    
		    pause()

def _ping():
    comm='ping -c 1 ' + par['ip']
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]		
    out = output.split('/')	
    return out[4]

def _err():
    dat = datetime.datetime.now().strftime("%d-%m-%Y")
    tim = datetime.datetime.now().strftime("%H:%M:%S")
    unerr = class_snmp._snmpwalk2(par['ip'],lib_oid.SQUnerroreds)
    corerr = class_snmp._snmpwalk2(par['ip'],lib_oid.SQCorrecteds)
    uncorerr = class_snmp._snmpwalk2(par['ip'],lib_oid.SQUncorrectables)
    ping = _ping()
    unerr = int(unerr)
    corerr = int(corerr)
    uncorerr = int(uncorerr)
    un = str(unerr)
    co = str(corerr)
    unco = str(uncorerr)

    ddd = dat+";"+un+";"+co+";"+unco+";"+ping+";"+"\n"
    print ddd
    class_log.create_csv2(ddd)

def _signal():
    dat = datetime.datetime.now().strftime("%d-%m-%Y")
    tim = datetime.datetime.now().strftime("%H:%M:%S")
    dsnr = class_snmp._snmpwalk2(par['ip'],lib_oid.SQSignalNoise)
    dpow = class_snmp._snmpwalk2(par['ip'],lib_oid.DownChannelPower)
    upow = class_snmp._snmpwalk2(par['ip'],lib_oid.CmStatusTxPower)
    ads = dsnr.split('\n') 
    adp = dpow.split('\n') 
    aup = upow.split('\n')
    for i in ads:
	print "Downstream channel . "+i
    for j in adp:
	print "Downstream snr channel . "+j
    for k in aup:
	print "Upstream channel . "+k

def _exec2(i,aaa):
    for a in lib_sw.CVE30360:	    		
	if a == i:
	    if aaa == "ts1":
		par['Test SW 01'] = a
	    if aaa == "ts2":
		par['Test SW 02'] = a
	    if aaa == "fs1":
		par['Field SW 01'] = a
	    if aaa == "fs2":
		par['Field SW 02'] = a

    for a in lib_sw.CH6640E:	    		
	if lib_sw.CH6640E[a] == i:	    
	    if aaa == "ts1":
		par['Test SW 01'] = lib_sw.CH6640E[a]
	    if aaa == "ts2":
		par['Test SW 02'] = lib_sw.CH6640E[a]
	    if aaa == "fs1":
		par['Field SW 01'] = lib_sw.CH6640E[a]
	    if aaa == "fs2":
		par['Field SW 02'] = lib_sw.CH6640E[a]
    for a in lib_sw.A6490:	    		
	if lib_sw.A6490[a] == i:	    
	    if aaa == "ts1":
		par['Test SW 01'] = lib_sw.A6490[a]
	    if aaa == "ts2":
		par['Test SW 02'] = lib_sw.A6490[a]
	    if aaa == "fs1":
		par['Field SW 01'] = lib_sw.A6490[a]
	    if aaa == "fs2":
		par['Field SW 02'] = lib_sw.A6490[a]
    for a in lib_sw.Ta7200K:	    		
	if lib_sw.Ta7200K[a] == i:	    
	    if aaa == "ts1":
		par['Test SW 01'] = lib_sw.Ta7200K[a]
	    if aaa == "ts2":
		par['Test SW 02'] = lib_sw.Ta7200K[a]
	    if aaa == "fs1":
		par['Field SW 01'] = lib_sw.Ta7200K[a]
	    if aaa == "fs2":
		par['Field SW 02'] = lib_sw.Ta7200K[a]

###########################tests############################


def cm_ver_homespot():
    if par['model'] == "CH6045":	
    	class_log.create_file("\n#\n#\t\t Verify the HOME SPOT  : \n#\n")
	class_log.create_file("#\n#\t\t GRE interfaces status : \n###################################################\n")
	aaa = class_snmp._snmpwalk2(par['ip'],lib_oid.CH6640E_greif)	
	if '1' in aaa:
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_greif)	
	    class_log.create_file("#\n#\t\t GRE names status : \n####################################################\n")
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_grename)
	    class_log.create_file("#\n#\t\t GRE fqdn : \n#######################################################\n")
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_fqdn) 
	    class_log.create_file("#\n#\t\t GRE package output : \n##################################################\n")
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_pckin)
	    class_log.create_file("#\n#\t\t GRE package input : \n###################################################\n")
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_pckout)
	    
	    print class_snmp._snmpwalk(par['ip'],lib_oid.CH6640E_ssid)
	else:
	    print "HOME SPOT : "+c.B+c.RED+"DOWN"+c.END
	    class_log.create_file("#\n#\t\t HOME SPOT is DOWN \n#####################################################\n")
    if par['model'] == "Ta7200K":
	print "unsupported"	

def cm_eventlogs_ext():
	class_log.create_file("\n#\n#\t\t Verify the DOCSIS Event Logs  : \n#\n")
	print class_snmp._snmpwalk(par['ip'],lib_oid._sysdescr)	
	if par['model'] == "CH6640E":
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.2.54') 
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.9.2') 
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.13.1.7') 
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.18.1') 
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.18.2') 
	    print class_snmp._snmpwalk(par['ip'],'1.3.6.1.4.1.35604.1.200.18.3') 
	print class_snmp._snmpwalk(par['ip'],lib_oid.Ev)	
	print class_snmp._snmpwalk4491(par['ip'],'1.3.6.1.4.1.4491')


def cm_signallevel():
	if par['dur']=="":
	    _signal()
	else:
	    w = par['dur']
	    w = int(w)
	    for i in range(1,w):
		os.system('clear')
		pro = 80/w
		pr = 100/w
		pp = pr * i
		pp = str(pp)
		pro = pro * i
		print c.B+c.GREEN+"="*pro+">>"+pp+"%"+c.END	
		_signal()		
		time.sleep(1)

def cm_reboot():
	q = '.'
	print class_snmp._snmpset(par['ip'],lib_oid.ResetNow,"integer","1")
	os.system('clear')	   
	print "Reboot NOW !!!" 
	re = "yes"
	time.sleep(5)
	while re == "yes":
	    time.sleep(1)
	    comm="ping -c 1 "+par['ip']+" >/dev/null && echo 'Y!'"
	    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
	    out=proc.communicate()[0]				    
	    out = out.rstrip("\r\n")
	    if out == "Y!":
		os.system('clear')	    
	        print c.B+c.GREEN+"CM online"+c.END
		re = "no"	    
	    else:
		os.system('clear')
		e = 'Reboot CM ['
		r = ']'	
		q += '.'
		print c.RED+c.B+e+q+r+c.END
    
def cm_sysdesc():
	class_log.create_file("\n#\n#\t\t System Description : \n#\n")
	print class_snmp._snmpwalk(par['ip'],lib_oid._sysdescr)    

def cm_status():
	class_log.create_file("\n#\n#\t\t Cable Modem Status : \n#\n")
	print class_snmp._snmpwalk(par['ip'],lib_oid.SwStatus)    
def cm_eventlogs():
    	class_log.create_file("\n#\n#\t\t Cable Modem Event log : \n#\n")
	print class_snmp._snmpwalk(par['ip'],lib_oid.EvText)
def cm_swup_test1():
	class_log.create_file("\n#\n#\t\t SW Update Downgrade to Version: "+par['Test SW 01']+"\n#\n")
	print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwFilename,"s",par['Test SW 01'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerTransportProtocol,"integer",par['swtransportprotocol'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddressType,"integer",par['swserveraddresstype'])
	#print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddress,"x","2A 02 81 00 C9 41 01 01 00 02 00 00 00 01 11 01")
	print class_snmp._snmpset(par['ip'],lib_oid.SwAdminStatus,"integer","1")
def cm_swup_test2():
	class_log.create_file("\n#\n#\t\t SW Update Downgrade to Version: "+par['Test SW 02']+"\n#\n")
	print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwFilename,"s",par['Test SW 02'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerTransportProtocol,"integer",par['swtransportprotocol'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddressType,"integer",par['swserveraddresstype'])
	#print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddress,"x","2A 02 81 00 C9 41 01 01 00 02 00 00 00 01 11 01")
	print class_snmp._snmpset(par['ip'],lib_oid.SwAdminStatus,"integer","1")
def cm_swup_f1():
	class_log.create_file("\n#\n#\t\t SW Update Downgrade to Version: "+par['Field SW 01']+"\n#\n")
	print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwFilename,"s",par['Field SW 01'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerTransportProtocol,"integer",par['swtransportprotocol'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddressType,"integer",par['swserveraddresstype'])
	#print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddress,"x","2A 02 81 00 C9 41 01 01 00 02 00 00 00 01 11 01")
	print class_snmp._snmpset(par['ip'],lib_oid.SwAdminStatus,"integer","1")

def cm_swup_f2():
	class_log.create_file("\n#\n#\t\t SW Update Downgrade to Version: "+par['Field SW 02']+"\n#\n")
	print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwFilename,"s",par['Field SW 02'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerTransportProtocol,"integer",par['swtransportprotocol'])
	print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddressType,"integer",par['swserveraddresstype'])
	#print class_snmp._snmpset(par['ip'],lib_oid.SwServerAddress,"x","2A 02 81 00 C9 41 01 01 00 02 00 00 00 01 11 01")
	print class_snmp._snmpset(par['ip'],lib_oid.SwAdminStatus,"integer","1")    

def box_cm():
    ips = class_snmp._snmpwalk2(par['ip'],lib_oid.box_IP_IF)
    macs = class_snmp._snmpwalk2(par['ip'],lib_oid.box_MAC_IF)
    all_parts = ips.split('\n')
    cpe_ip = str(all_parts[3])
    mta_ip = str(all_parts[2])
    cm_ip = str(all_parts[1])
    routers_ip = str(all_parts[0])
    #print class_snmp._snmpwalk3(mta_ip,"1.3.6.1.4.1.35604.1.200.2.54")
    print ips

####################################################################
def iftable23():
	class_log.create_file("\n#\n#\t\t 2.3.1.1 - ifTable IF-MIB (Docsis 2.0 and Docsis 3.0) Test : \n#\n")

	class_log.create_file("\n#\n#\t\t mactable : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.2.2.1.6.16')
	
	class_log.create_file("\n#\n#\t\t ??? : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.2.2.1')

	class_log.create_file("\n#\n#\t\t docsifDownstreamChannelTable : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.10.127.1.1.1')
	
	class_log.create_file("\n#\n#\t\t docsifUpstreamChannelTable: \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.10.127.1.1.2')
	
	class_log.create_file("\n#\n#\t\t docsifSignalQualityTable : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.10.127.1.1.4')
	
	class_log.create_file("\n#\n#\t\t docsifCmMacTable : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.10.127.1.2.1')
	
	class_log.create_file("\n#\n#\t\t docsifCmStatusTable : \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.10.127.1.2.2')
	
	class_log.create_file("\n#\n#\t\t sysUptime: \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.1.3.0')
	
	class_log.create_file("\n#\n#\t\t sysName: \n#\n")
	print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.1.5.0')
	#print class_snmp._snmpwalk(par['ip'],'1.3.6.1.2.1.2.2.1.6.16')
	 

def iftable3():
	print "aa"

def docscabledevice():
	print "bb"

def docsif3mib():
	print "ccc"
####################################################################

    #print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])

def box_cpe():
    print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])

def box_mta():
    print class_snmp._snmpset(par['ip'],lib_oid.SwServer,"a",par['tftpd'])

def _exec(i):
    if i == "Test duration":
	par['dur'] = raw_input('Please enter test duration in minutes : ')
    if i =="IP address":
	par['ip'] = raw_input('Please enter cable modem ip : ')
    if i =="MAC address":
	par['mac'] = raw_input('Please enter cable modem mac : ')
    if i =="TFTPD address":
	par['tftpd'] = raw_input('Please enter tftpd : ')
    if i =="Cable Modem Part Information":
	class_Ta1.cm_info(par)
    if i =="Verify HOME SPOT":
	cm_ver_homespot()	    
    if i =="Verify the DOCSIS Event Logs":
	cm_eventlogs_ext()
    if i =="Signal Test":
	cm_signallevel()
    if i == "Reboot":
	cm_reboot()			
    if i == "System Description":
	cm_sysdesc()
    if i == "Cable Modem Status":	
	cm_status()
    if i == "Cable Modem Event Log":
	cm_eventlogs()
#####################sw test#########################
    if i == "cm sw update test01":
	cm_swup_test1()
    if i == "cm sw update test02":
	cm_swup_test2()
    #################CMTS########################
    if i == "scm":
	print cmtsssh.connect("show cable modem") 
    if i == "cpe":
    	if par['mac']=='':
	    print cmtsssh.connect("show cable modem "+ par['ip'])
	else:
    	    print cmtsssh.connect("show cable modem "+ par['ip'])
    if i == "cpe ipv6":
    	if par['mac']=='':
	    print cmtsssh.connect("show cable modem "+ par['ip'])
	else:
	    print cmtsssh.connect("show cable modem "+ par['ip'])
    if i == "cpe qos":
    	if par['mac']=='':
    	    print cmts.scm_qos(par['ip'])
	else:
	    print cmts.scm_qos(par['mac'])
    if i == "cpe details":
	if par['mac']=='':
	    print cmts.scm_v4(par['ip'])    	
	else:
    	    print cmts.scm_v4(par['mac'])    	
    ##########################################BOX TESTs

    ###############################################

#####################################
    if i =="2.12.2 The firmware information in the SNMP MIB SysDescr.0 MUST be displayes as":
	cm_sysdesc()
    if i =="2.3.1.1 ifTable IF-MIB (Docsis - 2.0 and 3.0)":
	iftable23()
	