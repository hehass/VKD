
cmtest = {'Cable Modem Status':'','Cable Modem Event Log':'','Cable Modem SW Update':'',
	 'Cable Modem makro 1 Test':'','Cable Modem makro 2 Test':'','Reboot':'','Exit':''}
main = {
	1:'2.01.01 CM and MTA Status out of the box',
	2:'2.02 Check of DHCP criteria',
	3:'2.03 SNMP: Reas OIDs via SNMP after Provisioning',
	4:'2.04 GUI checks from WAN - LAN',   
        	5:'2.05 FTP - iperf Speedtest',
	6:'2.06 Firmware Up - Downgrades',
	7:'2.07 Tariff checks',
	8:'2.08 Functional Box test',
	9:'2.09 Ccc',
	10:'2.10',
	11:'2.11 TestCases1',
	12:'2.12 Firmware Upgrade and Dwongrade Conventions',
	13:'2.13 Remote Management & Monitoring'}


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

def _logo(tab):
    char = chr(255)
    print char*80
    print c.B + c.RED + 'Vendor : ' + c.END + tab['vendor'] + c.B + c.RED + '\tModel : ' + c.END + tab['model'] 
    print c.B + c.RED + 'IPv ' + tab['ipv'] + ' CM IP : ' + c.END + tab['ip'] + '\t SW : ' +c.RED+c.B+tab['mac']+c.END 
    print c.RED + "" + c.B + 'TFTPD' + c.END + ' IP :' + tab['tftpd'] +c.RED+ "\tServer Transport: "+c.END +tab['swtransportprotocol'] + c.RED +"\tServer adress type : "+c.END + tab['swserveraddresstype']
    print c.GREEN+c.B + "Test Firmware 01 : " + c.END + tab['Test SW 01'] 
    print c.GREEN+c.B + "Test Firmware 02 : " + c.END + tab['Test SW 02'] 
    print c.RED + "" + c.B + 'Test Duration :'+ tab['dur'] + c.END + "LOG NAME : "+tab['tc']
    print char*80

def draft(_cm):
    print ""
    for a in _cm:
	b = str(a)
        print "\t\t" +c.B +"" + _cm[a] + ": ( "+c.RED+""+b+" )" + c.END
    print "\t\t"+c.B+"Exit" + c.RED + "(q)"+ c.END   

def _main(main):
    print ""
    for a in main:
	b = str(a)
        print "\t\t" +c.B +"" + main[a] + ": ( "+c.RED+ b +" )" + c.END
    print "\t\t"+c.B+"Exit" + c.RED + "(q)"+ c.END   
    
#def _cmtstest():
