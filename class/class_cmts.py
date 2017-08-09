#!/usr/bin/python
 
import telnetlib
import datetime
import sys
sys.path.append('/home/testing/Ta/class')
import class_log
#import paramiko

#######temporary 

host = "10.154.100.2" # your router ip
password = "fredfred"

def cmts_read(comm):

    tn = telnetlib.Telnet(host)
    tn.read_until("Password:")
    tn.write(password+"\n")
    tn.write("enable"+"\n")
    tn.read_until("Password:")
    tn.write(password+"\n")
    tn.write("terminal length 0"+"\n")
    tn.write(comm)
    tn.write("exit"+"\n")    
    ret = tn.read_all()
    class_log.create_file(ret)
    print ret	

class cmts_ssh:
    def connect(self,command):
	
	password = "fredfred"
	username = "hhellebrand"
	port = 22
	cmts = "10.154.100.2"
	print command
	try:
	    client = paramiko.SSHClient()
	    client.load_system_host_keys()
	    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
	    client.connect(cmts, port=port, username=username, password=password)
 
	    stdin, stdout, stderr = client.exec_command(command)
	    print stdout.read(), 

	finally:
	    client.close()


class cmts: 
    def scm(self):
        comm = "sh cable modem"+"\n"
        cmts_read(comm)

    def scm_v4(self,ip):
        comm = "sh cable modem " + ip + " cpe \n"
        cmts_read(comm)
    
    def scm_v6(self,ip):
	comm = "sh cable modem " + ip + " ipv6 cpe \n"
	cmts_read(comm)

    def scm_qos(self,ip):
	comm = "sh cable modem " + ip + " qos \n"
	cmts_read(comm)

    def scm_c4(self,ip):
	comm = "sh cable modem " + ip + " details \n"
	cmts_read(comm)