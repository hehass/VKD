#!/usr/bin/python

import sys
import subprocess
sys.path.append('/home/testing/Ta/class')
sys.path.append('/home/testing/Ta/libs')
import lib_oid
import class_log





params = {	'ip':'',
		'mac':'',
		'read_c':'public',				
		'write_c':'public'
	 }

def _snmpget2(inn,oid):
    comm='snmpget -Oqv -v2c -c ' + params['read_c'] + ' ' + inn + ' ' + oid
    #print comm
    #class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    #class_log.create_file(output)
    return output

def _snmpwalk2(inn,oid):
    comm='snmpwalk -Oqv -v2c -c ' + params['read_c'] + ' ' + inn + ' ' + oid
    #class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    #class_log.create_file(output)
    return output

def _snmpwalk3(inn,oid):
    comm='snmpwalk -Oqv -v2c -c ' + params['write_c'] + ' ' + inn + ' ' + oid
    #class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    #class_log.create_file(output)
    return output

def _snmpwalk4(inn,oid):
    comm='snmpwalk -Ov -v2c -c ' + params['write_c'] + ' ' + inn + ' ' + oid
    #class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    #class_log.create_file(output)
    return output

def _snmpwalk4491(inn,oid):
    comm='snmpwalk -v2c -c ' + params['read_c'] + ' ' + inn + ' ' + oid
    #class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    class_log.extra_4491(output)
    return output

def _snmpget(inn,oid):
    comm='snmpget -v2c -c ' + params['read_c'] + ' ' + inn + ' ' + oid
    class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    class_log.create_file(output)			
    return comm + "\n" + output + "\n"

def _snmpwalk(inn,oid):
    comm='snmpwalk -v2c -c ' + params['read_c'] + ' ' + inn + ' ' + oid
    class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    class_log.create_file(output)
    return comm + "\n" + output + "\n"

def _snmpwalk_(inn,oid):
    comm='snmpwalk -v2c -c ' + params['write_c'] + ' ' + inn + ' ' + oid
    class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    class_log.create_file(output)
    return comm + "\n" + output + "\n"

def _snmpset(inn,oid,var,val):
    comm='snmpset -v2c -c ' + params['write_c'] + ' ' + inn + ' ' + oid + ' ' + var + ' ' + val
    class_log.create_file("\n" + comm + "\n")
    proc=subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]			
    class_log.create_file(output)
    return comm + "\n" + output + "\n"

class snmp:    
    def read_oid(inn,self):
	oid = lib_oid._oid
	return _snmpget2(inn,oid)

    def read_vendor(inn,self):
	oid = lib_oid._vendor
	return _snmpget2(inn,oid)

    def read_model(inn,self):
	oid = lib_oid._model
	return _snmpget2(inn,oid)

    def read_cmmac(self):
	print "tset"

#class sw_update: 

class sw_change:
    def cm_status(self):
	oid = oidlib._cm_status
	return _snmpwalk(oid)

    def cm_log(self):
	oid = oidlib._cm_log_checker
	return _snmpwalk(oid)

    ####################################

    def cm_tftp(self):
	oid = oidlib._cm_tftp_address
	typee = "a"
	value = iplib._tftpd1	
	return _snmpset(oid,typee,value)

    def cm_set_firmware(self):
	oid = oidlib._cm_set_firmware   
	typee = "a"
	value = iplib._sw1	
	return _snmpset(oid,typee,value)

    def cm_set_address_type(self):
	oid = oidlib._cm_set_address_type  
	typee = "a"
	value = "1"	
	return _snmpset(oid,typee,value)    

    def cm_start_update(self):
	oid = oidlib._cm_start_downgrade
	typee = "a"
	value = "1"
	return _snmpset(oid,typee,value)    
	###############################################

    def cm_sw_update(self):
	sw_change.cm_tftp()
	cm_firmware()
	cm_set_address_type()	
	
    

