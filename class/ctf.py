import curses                                                                
from curses import panel                                                     
import os
import sys
import time
import datetime
import subprocess
import operator
sys.path.append('../libs')
import lib_menu
import lib_oid
import lib_sw
import class_log
import class_snmp
import class_cmts

snmp = class_snmp.snmp()
cmts = class_cmts.cmts()

