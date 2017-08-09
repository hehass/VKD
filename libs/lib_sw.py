
###########compal##################

models = {'CVE30360':'Hitron',
'CGNV4':'KDHitron', 
'CH6640E':'Compal', 
'CH7466CE':'Compal', 
'6360':'AVM', 
'6490':'AVM', 
'7270':'AVM', 
'THG520':'Technicolor',
'THG540':'Technicolor',
'THG541':'Technicolor',
'THG570':'Technicolor',
'THG571':'Technicolor',
'TC7200K':'Technicolor',
'TC720020':'Technicolor'
}

CVE30360 = {
				    "3.1.1.11-MGCP-KDG" : "cve-30360-3.1.1.11-mgcp-kdg-110926-euro.sbn", #//
				    "3.1.1.12-MGCP-KDG" : "cve-30360-3.1.1.12-mgcp-kdg-111205-euro.sbn", #// update uz: 21.2.2013, introduced factory firmware
				    "3.1.1.15-MGCP-KDG" : "CVE-30360-3.1.1.15-MGCP-KDG-120607-EURO.sbn",
				    "3.1.1.21-MGCP-KDG" : "CVE-30360-3.1.1.21-MGCP-KDG-121126-EURO.sbn",
				    "3.1.1.21-MGCP-KDG-EC1" : "CVE-30360-3.1.1.21-MGCP-KDG-EC1-130710.sbn",
				    "3.1.1.21-MGCP-KDG-EC2" : "CVE-30360-3.1.1.21-MGCP-KDG-EC2-130725.sbn",
				    "3.1.1.23-MGCP-KDG-T4" : "cve-30360-3.1.1.23-mgcp-kdg-t4-130111.sbn",
				    "3.1.1.21-preT2-IMS-KDG" : "CVE-30360-3.1.1.21-preT2-IMS-KDG-130111.sbn",
				    "3.1.1.21-T2-IMS-KDG" :"CVE-30360-3.1.1.21-T2-IMS-KDG-130130.sbn", #// update uz: 5.2.2013
				    "3.1.1.21-T3-IMS-KDG" :"CVE-30360-3.1.1.21-T3-IMS-KDG-130308.sbn",
				    "3.1.1.21-T4-IMS-KDG" :"CVE-30360-3.1.1.21-T4-IMS-KDG-130402.sbn",
				    "3.1.1.21-T5-IMS-KDG" :"CVE-30360-3.1.1.21-T5-IMS-KDG-130417.sbn",
				    "3.1.1.21-T7-IMS-KDG" :"CVE-30360-3.1.1.21-T7-IMS-KDG-130516.sbn",
				    "3.1.1.21-T8-IMS-KDG" :"CVE-30360-3.1.1.21-T8-IMS-KDG-130521.sbn",
				    "3.1.1.21-T9-IMS-KDG" :"CVE-30360-3.1.1.21-T9-IMS-KDG-130524.sbn",
				    "3.1.1.22-IMS-KDG" : "CVE-30360-3.1.1.22-IMS-KDG-130528.sbn",
				    "3.1.1.22-T2-IMS-KDG" : "CVE-30360-3.1.1.22-T2-IMS-KDG-130614.sbn",
				    "3.1.1.22-T3-IMS-KDG" : "CVE-30360-3.1.1.22-T3-IMS-KDG-130627.sbn",
				    "3.1.1.23-IMS-KDG" : "CVE-30360-3.1.1.23-IMS-KDG-130628.sbn",
				    "3.1.1.23-T1-IMS-KDG" : "CVE-30360-3.1.1.23-T1-IMS-KDG-130715.sbn",
				    "3.1.1.24-IMS-KDG" : "cve-30360-3.1.1.24-ims-kdg-130719.sbn",
				    "3.1.1.25-IMS-KDG" : "cve-30360-3.1.1.25-ims-kdg-130725.sbn",
				    "3.1.1.26-IMS-KDG" : "CVE-30360-3.1.1.26-IMS-KDG-130807.sbn",
				    "3.1.1.26-T2-IMS-KDG" : "CVE-30360-3.1.1.26-T2-IMS-KDG-130917.sbn",
				    "3.1.1.27-T1-IMS-KDG" : "CVE-30360-3.1.1.27-T1-IMS-KDG-131017.sbn",
				    "3.1.1.28-T2-IMS-KDG" : "CVE-30360-3.1.1.28-T2-IMS-KDG-131105.sbn",
				    "3.1.1.29-IMS-KDG" : "CVE-30360-3.1.1.29-IMS-KDG-131106.sbn",
				    "3.1.1.29-3wc-IMS-KDG" : "CVE-30360-3.1.1.29-3wc-IMS-KDG-131205.sbn",
				    "3.1.1.29-00-IMS-KDG" : "CVE-30360-3.1.1.29-00-IMS-KDG-140207.sbn", #  // 07.02.2014 Tobias: new 00 debugging image from 140207 //
				    "3.1.1.30-IMS-KDG" : "CVE-30360-3.1.1.30-IMS-KDG-140120.sbn",  #/* 2014-01-22 Uwe: added new firmware */
				    "3.1.1.30-00fix-IMS-KDG" : "CVE-30360-3.1.1.30-00fix-IMS-KDG-140213.sbn",
				    "4.2.8.2-IMS-KDG" : "CVE-30360_4.2.8.2-IMS-KDG-anonymous-140210.sbn",
				    "4.2.8.3-IMS-KDG-T2" : "CVE-30360_4.2.8.3-IMS-KDG-T2-140212.sbn",
				    "3.1.1.31-IMS-KDG" : "CVE-30360-3.1.1.31-IMS-KDG-140224.sbn",
				    "4.2.8.3-IMS-KDG" : "CVE-30360_4.2.8.3-IMS-KDG-140227.sbn",
				    "4.2.8.4-IMS-KDG" : "CVE-30360_4.2.8.4-IMS-KDG-140228.sbn",
				    "4.2.8.4-IMS-test-iprule-KDG" : "CVE-30360_4.2.8.4-IMS-test-iprule-KDG-140314.sbn",
				    "4.2.8.5-IMS-KDG" : "CVE-30360_4.2.8.5-IMS-KDG-140321.sbn",
				    "4.2.8.5-IMS-KDG-for_ip_pref-test" : "CVE-30360_4.2.8.5-IMS-KDG-140404-for-ip-pref-test.sbn",
				    "4.2.8.6-IMS-KDG" : "CVE-30360_4.2.8.6-IMS-KDG-140410.sbn",
				    "4.2.8.6-IMS-KDG-174" : "CVE-30360_4.2.8.6-IMS-KDG-140424-KDG-174.sbn",
				    "4.2.8.7-IMS-KDG-T1" : "CVE-30360_4.2.8.7-IMS-KDG-T1-140425.sbn",
				    "4.2.8.7-IMS-KDG-T1-bccrashfix" : "CVE-30360_4.2.8.7-IMS-KDG-T1-bccrashfix-140430.sbn",
				    "4.2.8.7-IMS-KDG-T1_tlv5" : "CVE-30360_4.2.8.7-IMS-KDG-T1-140506-for-ipv6-tlv5-test.sbn",
				    "4.2.8.7-IMS-KDG-T1_140508" : "CVE-30360_4.2.8.7-IMS-KDG-T1-140508-for-ipv6-eDVA.sbn", #// another attempt for IPv6 prov. eDVA
				    "4.2.8.7-IMS-KDG-T2" : "CVE-30360_4.2.8.7-IMS-KDG-T2-140509.sbn",
				    "4.2.8.7-IMS-KDG" : "CVE-30360_4.2.8.7-IMS-KDG-140516.sbn",
				    "4.2.8.7-IMS-KDG-for-dslite-dns-query" : "CVE-30360_4.2.8.7-IMS-KDG-for-dslite-dns-query.sbn",
				    "4.2.8.8-IMS-KDG-for-route-port" : "CVE-30360_4.2.8.8-IMS-KDG-T1-140619-for-route-port.sbn",# // now with corrected sip message for IPv6 prov. eDVA
				    "4.2.8.8-IMS-KDG-for-all-bugfixes" : "CVE-30360_4.2.8.8-IMS-KDG-T3-140625.sbn",
				    "4.2.8.8-IMS-KDG-for-ipv6-gssp" : "CVE-30360_4.2.8.8-IMS-KDG-T3-140625-for-ipv6-gssp.sbn",
				    "4.2.8.8-IMS-KDG-T4" : "CVE-30360_4.2.8.8-IMS-KDG-T4-140703.sbn",
				    "4.2.8.8-PCP-T1-KDG" : "CVE-30360_4.2.8.8-PCP-T1-KDG-140807.sbn",
				    "4.2.8.8-IMS-KDG" : "CVE-30360_4.2.8.8-IMS-KDG-140808.sbn", #// oneikes 2014-08-11: release version for next official release
				    "4.2.8.9-IMS-KDG" : "CVE-30360_4.2.8.9-IMS-KDG-140813.sbn",  #// tkolbe  2014-08-18: official release version (based on Intel SDK4.2)
				    "4.2.8.9-IMS-KDG-ST1" : "CVE-30360_4.2.8.9-IMS-KDG-ST1-140819.sbn",  #// tkolbe  2014-08-18: eng release for speedtest issue
				    "4.2.8.9-IMS-KDG-failover" : "CVE-30360_4.2.8.9-IMS-KDG-failover-140909.sbn",  #// tkolbe  2014-08-18: eng release for re-register issue
				    "4.2.8.9-IMS-KDG-phone-test" : "CVE-30360_4.2.8.9-IMS-KDG-140905-for-phone-date-test.sbn",  #// tkolbe  2014-08-18: eng release for fsk signalling phone test 
				    "4.2.8.9-IMS-KDG-PCP-OPTION86-140915" : "CVE-30360_4.2.8.9-IMS-KDG-PCP-OPTION86-140915.sbn", #// oneikes 2014-09-16: eng release for dhcpv6 option 86 (pcp)
				    "4.2.8.9-IMS-KDG-GREv6" : "CVE-30360_4.2.8.9-IMS-KDG-GREv6-2-140901.sbn", #// AFH IPv6 GRE
				    "4.2.8.10-IMS-KDG" : "cve-30360_4.2.8.10-ims-kdg-140919.sbn", #// hsiegert 2014-09-22: release version for next official release
				    "4.2.8.10-USFW-IMS-KDG" : "CVE-30360_4.2.8.10-USFW-IMS-KDG-141029.sbn", #// aguenther 2014-11-03: eng version perf issue
				    "4.2.8.10-IMS-KDG-HP1" : "CVE-30360_4.2.8.10-IMS-KDG-HP1-141023.sbn", #//julrich 2014-11-14: eng version Host Port feature
				    "4.2.8.11-IMS-KDG" : "CVE-30360_4.2.8.11-IMS-KDG-141114.sbn", # //julrich 2015-02-17: eng version
				    "4.2.8.12-IMS-KDG" : "CVE-30360_4.2.8.12-IMS-KDG-141118.sbn", #//julrich 2014-11-24: official release version
				    "4.2.8.12-IMS-KDG-reboot" : "CVE-30360_4.2.8.12-IMS-KDG-reboot-T1-141212.sbn",
				    "4.2.8.12-IMS-KDG-reboot-T2" : "CVE-30360_4.2.8.12-IMS-KDG-reboot-T2-141219.sbn",
				    "4.2.8.13-IMS-KDG" : "CVE-30360_4.2.8.13-IMS-KDG-150128.sbn", #//julrich 2015-01-28: official release version
				    "4.2.8.14-IMS-KDG" : "CVE-30360_4.2.8.14-IMS-KDG-150211.sbn"  #//julrich 2015-02-12: official release version				
}
CGNV4KD = {
				    "4.4.10.1-IMS-KDG" : "CGNV4-KD_4.4.10.1-IMS-KDG-141205.sbn",   # // 08.12.2014 oneikes: Initial engineering release
				    "4.4.10.3-IMS-KDG" : "CGNV4-KD_4.4.10.3-IMS-KDG-150109.sbn",   # // 12.01.2015 oneikes: New engineering release
				    "4.4.10.4-IMS-KDG-T1" : "CGNV4-KD_4.4.10.4-IMS-KDG-T1-150116.sbn", #   // 19.01.2015 julrich: New engineering release Add MTA MAC
				    "4.5.10.4-IMS-PCM" : "CGNV4-KD_4.5.10.4-IMS-PCM-150212.sbn",    #// 13.02.2015 julrich: New engineering release
				    "4.5.10.6-IMS-PCM-T1" : "CGNV4-KD_4.5.10.6-IMS-PCM-T1-150306.sbn"   # // 06.03.2015 julrich: New eng. release DHCPv6 Suboption 39				
}
CH6640E = {
"CH6640-3.1.5.16-NOSH" : "CH6640-3.1.5.16-NOSH-TW.NNEMN.p7",
				    "CH6640-3.1.5.9f-SH" : "ch6640-3.1.5.9f-sh-tw.nnemn.p7",  #// NCS.15 production firmware update HSG: 27.03.2014
				    "CH6640-3.5.0.3-NOSH" : "CH6640-3.5.0.3-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.0.4a-SH" : "CH6640-3.5.0.4a-SH-TW.NNEMN.p7", #// special firmware update uz: 14.2.2013
				    "CH6640-3.5.0.9b-SH" : "CH6640-3.5.0.9b-SH-TW.NNEMN.p7", #// special firmware update uz: 14.2.2013
				    "CH6640-3.5.0.10-NOSH" : "CH6640-3.5.0.10-NOSH-TW.NNEMN.p7",# // special firmware update ju: 25.2.2013
				    "CH6640-3.5.0.11b-SH" : "CH6640-3.5.0.11b-SH-TW.NNEMN.p7",# // special firmware update ju: 26.2.2013
				    "CH6640-3.5.0.12-NOSH" : "CH6640-3.5.0.12-NOSH-TW.NNEMN.p7", #// new official test firmware ju: 06.03.2013
				    "CH6640-3.5.0.12f-NOSH" : "CH6640-3.5.0.12f-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.0.12g-NOSH" : "CH6640-3.5.0.12g-NOSH-TW.NNEMN.p7",
                                    "CH6640-3.5.0.12h-NOSH" : "CH6640-3.5.0.12h-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.0.16g-SH" : "CH6640-3.5.0.16g-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1c-SH" : "CH6640-3.5.10.1c-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1e-SH" : "CH6640-3.5.10.1e-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1f-SH" : "CH6640-3.5.10.1f-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1g-SH" : "CH6640-3.5.10.1g-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1h-SH" : "CH6640-3.5.10.1h-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1k-SH" : "CH6640-3.5.10.1k-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1m-SH" : "CH6640-3.5.10.1m-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1n-SH" : "CH6640-3.5.10.1n-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1r-SH" : "CH6640-3.5.10.1r-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1s-SH" : "CH6640-3.5.10.1s-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.1u-SH" : "CH6640-3.5.10.1u-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.3-NOSH" : "CH6640-3.5.10.3-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.4-NOSH" : "CH6640-3.5.10.4-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.4a-SH" : "CH6640-3.5.10.4a-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.4b-SH" : "CH6640-3.5.10.4b-SH-TW.NNEMN.p7",
				    "CH6640-3.5.10.5-NOSH" : "CH6640-3.5.10.5-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.6-NOSH" : "CH6640-3.5.10.6-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.7-NOSH" : "CH6640-3.5.10.7-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.8-NOSH" : "CH6640-3.5.10.8-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.10.8a-SH" : "CH6640-3.5.10.8a-SH-TW.NNEMN.p7", #//Test FW DHCP Option 100, 101, oneikes 09.10.2013
				    "CH6640-3.5.10.9-NOSH" : "CH6640-3.5.10.9-NOSH-TW.NNEMN.p7",  # // PC2.0 + Homespot image + Patch US partial service problem; 21.10 aguenther
				    "CH6640-3.5.10.10-NOSH" : "CH6640-3.5.10.10-NOSH-TW.NNEMN.p7", #// PC2.0 + Homespot image + Patch ID112: DHCP Option82 ; oneikes 08.11.2013
				    "CH6640-3.5.11.1a-SH" : "CH6640-3.5.11.1A-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.1b-SH" : "CH6640-3.5.11.1b-SH-TW.NNEMN.p7",
				    "CH6640-3.5.1.4b-SH" : "CH6640-3.5.1.4b-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.2-SH" : "CH6640-3.5.11.2-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.3-SH" : "CH6640-3.5.11.3-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.3a-SH" : "CH6640-3.5.11.3a-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.3b-SH" : "CH6640-3.5.11.3b-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.4-NOSH" : "CH6640-3.5.11.4-NOSH-TW.NNEMN.p7",   #// new official test firmware JUL: 20.03.2014
				    "CH6640-3.5.11.4a-SH" : "CH6640-3.5.11.4a-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.4b-SH" : "CH6640-3.5.11.4b-SH-T.NNEMN.p7",
				    "CH6640-3.5.11.5-NOSH" : "CH6640-3.5.11.5-NOSH-TW.NNEMN.p7",
				    "CH6640-3.5.11.5a-SH" : "CH6640-3.5.11.5a-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.6-SH" : "CH6640-3.5.11.6-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.6-NOSH" : "CH6640-3.5.11.6-NOSH-TW.NNEMN.p7", #// official release, oneikes:  05.06.2014
				    "CH6640-3.5.11.7-NOSH" : "CH6640-3.5.11.7-NOSH-TW.NNEMN.p7", #// official release, JUL:  16.06.2014
				    "CH6640-3.5.11.7a-SH" : "CH6640-3.5.11.7a-SH-TW.NNEMN.p7", #// engineering release with Option 82 for FixIP, oneikes 25.07.2014
				    "CH6640-3.5.11.7b-SH" : "CH6640-3.5.11.7b-SH-TW.NNEMN.p7", #// engineering release with advanced PCP, oneikes 12.08.2014
				    "CH6640-3.5.11.7c-SH" : "CH6640-3.5.11.7c-SH-TW.NNEMN.p7", #// engineering release DNS fix, JUL 19.08.2014
				    "CH6640-3.5.11.8-NOSH" : "CH6640-3.5.11.8-NOSH-TW.NNEMN.p7", #// official release, JUL: 01.10.2014
				    "CH6640-3.5.11.8-SH" : "CH6640-3.5.11.8-SH-TW.NNEMN.p7",
				    "CH6640-3.5.11.9-NOSH" : "CH6640-3.5.11.9-NOSH-TW.NNEMN.p7",# // official release DHCPv4 fix, JUL: 02.10.2014
				    "CH6640-3.5.11.9-SH" : "CH6640-3.5.11.9-SH-TW.NNEMN.p7",
				    "CH6640-3.5.12.0a-SH" : "CH6640-3.5.12.0a-SH-TW.NNEMN.p7",# // engineering release with support voice over IPv6, oneikes: 25.06.2014
				    "CH6640-4.5.0.0c-SH" : "CH6640-4.5.0.0c-SH-TW.NNEMN.p7", #//engineering release, JUL: 09.02.2014
				    "CH6640-4.5.0.0e-SH" : "CH6640-4.5.0.0e-SH-TW.NNEMN.p7",	# //engineering release, JUL: 03.03.2014
				    "CH6640-4.5.0.1a-SH" : "CH6640-4.5.0.1a-SH-TW.NNEMN.p7"	 #//engineering release, JUL: 17.03.2014
				

}
CH7466CE = {
				    "CH7466CE-4.50.18.2-IMS-KDG-SH":"CH7466CE_4.50.18.2-IMS-KDG-20141227-SH.p7",	#	// 02.02.2015  default firmware
				    "CH7466CE-4.50.18.4-IMS-KDG-SH":"CH7466CE_4.50.18.4-IMS-KDG-20150129-SH.p7",	#	// 30.01.2015 Olaf: production firmware
				    "CH7466CE-4.50.18.4-IMS-KDG-NOSH":"CH7466CE_4.50.18.4-IMS-KDG-20150202-NOSH.p7",	#// 30.01.2015 Olaf: production firmware
				    "CH7466CE-4.50.18.4a-IMS-KDG-SH":"CH7466CE_4.50.18.4a-IMS-KDG-20150130-SH.p7",	#// 30.01.2015 Jrg: factory firmware
				    "CH7466CE-4.50.18.5-IMS-KDG-SH":"CH7466CE-4.50.18.5-IMS-KDG-20150213-SH.p7",	#	// 16.02.2015 : Eng. release
				    "CH7466CE-4.50.18.6-IMS-KDG-SH":"CH7466CE-4.50.18.6-IMS-KDG-20150217-SH.p7",
				    "4.50.18.7-IMS-KDG-SH":"CH7466CE-4.50.18.7-IMS-KDG-20150305-SH.p7",			#	// 06.03.2015 : production firmware
				    "4.50.18.7-IMS-KDG":"CH7466CE-4.50.18.7-IMS-KDG-20150305.p7"				#		// 06.03.2015 Jrg: production firmware				
}

A6360 = {
				    "85.05.22" : "6360.85.05.22.073008002010.cvc",
				    "85.05.29-24339" : "6360.85.05.29-24339.073008002010.cvc",
				    "85.05.29" : "6360.85.05.29.073008002010.cvc",
				    "85.05.50" : "6360.85.05.50.073008002010.cvc",	#	// new test firmware 
				    "85.05.51" : "6360.85.05.51-25122M.073008002010.cvc", # //test fw private IP Voice
				    "85.05.55" : "6360.85.05.55.073008002010.cvc",		#//release fw
				    "85.05.55-25906" : "6360.85.05.55-25906.073008002010.cvc",  # //20130820 drohrschneider HB2 KDGID 133 139//
				    "85.05.56" : "6360.85.05.56.073008002010.cvc",		#// 2013-09-19 oneikes: release fw
				    "85.05.59-26630" : "6360.85.05.59-26630.073008002010.cvc", #//2013-10-25 drohr: newest lab fw
				    "85.06.01" : "6360.85.06.01.073008002010.cvc",		#// 2013-12-02 H.Siegert: release fw
				    "85.06.01M" : "6360.85.06.01-27062M.073008002010.cvc", #//2014-01-09 drohr: acs url fix for ipv4 
				    "85.06.02" : "6360.85.06.02.073008002010.cvc",	#	// 2013-12-02 H.Siegert: release fw
				    "85.06.04" : "6360.85.06.04.073008002010.cvc",		#// 2014-02-10 Uwe Zellmer: release fw
				    "85.05.57" : "6360.85.05.57.073008002010.cvc",		#// 2014-02-12 J. Ulrich
				    "audioloss" : "6360.85.06.04_4474.073008002010.cvc",	#// 2014-03-19 drohr: audioloss fix partial service upstream
				    "85.06.05" : "6360.85.06.05.073008002010.cvc",		#// 2014-04-11 J. Ulrich: Fix partial service upstream
				    "85.06.10-28352" : "6360.85.06.10-28352.073008002010.cvc", #// 2014-08-21 drohr: upstream bonding
				    "85.06.10-28539" : "6360.85.06.10-28539.073008002010.cvc"  #// 2014-10-15 drohr: other upstream issue fw
			    
}
A6490 = {
				    "132.05.01" : "6490.132.05.01.073008002010.cvc",	#	// 09.01.2014: T.Kolbe: fake FW update file
				    "132.05.60"	: "6490.132.05.60-27288.120308002013.cvc",#  //05.02.2014 drohr: ACS URL generation included
				    "132.05-27583" : "6490.132.05.60-27583.120308002013.cvc",#  //26.02.2014 drohr: new fw wie immer ohne infos
				    "141.05.60" : "6490.141.05.60-27885.120308002013.cvc",	#// 15.04.2014 drohr: new fw Intel SDK 4.3.0.37, webinterface ueber kabel.box
				    "141.05.60-27885" : "6490.141.05.60-27885.120308002013.cvc",	#// 2014-04-24 Uwe: align with DHCPv4 information sw version in bac			
				    "141.05.60-27967" : "6490.en-de.141.05.60-27967.120308002013.cvc",	#// 2014-05-12 Tobias: new eng release for 6490	
				    "international"	  : "6490.141.05.60-27967.120308002013.cvc",#		// 2014-05-12 drohr: internationale version mit allem 
				    "141.05.60-28007" : "6490.141.05.60-28007.120308002013.cvc",   #//2014-05-20 drohr: LKZ OKZ FIX
				    "141.05.61"		  : "6490.141.05.61.120308002013.cvc",  			#//2014-05-23 drohr: RC1 fr FUT FW
				    "141.05.61-28139" : "6490.141.05.61-28139.120308002013.cvc",		#//2014-06-06 drohr: edva fix 
				    "141.05.61-28165" : "6490.141.05.61-28165.120308002013.cvc",		#//2014-06-10 drohr: offizielle Labversion mit edva fix ohne extras
				    "141.06.06"       : "6490.141.06.06.120308002013.cvc",				#//2014-06-16 drohr: offizielle Release FW fr Abnahmetest
				    "141.06.06-28204" : "6490.141.06.06-28204.120308002013.cvc",		#//2014-06-23 drohr: eng drop mit Homespot
				    "141.06.07"       : "6490.141.06.07.120308002013.cvc",				#//2014-07-01 drohr: offizielle Release FW ohne DVBC
				    "141.06.08"       : "6490.en-de-es-it-fr.141.06.08.120308002013.cvc", #//2014-07-21 oneikes: offizielle Release FW 
				    "141.06.08-28417" : "6490.en-de-es-it-fr.141.06.08-28417.120308002013.cvc", #//unofficial firmware by AVM 20140804
				    "141.06.09-28594" : "6490.141.06.09-28594.120308002013.cvc", 		#//fix fr RN 199/ Speedtest Port/ Homespot nur ein reboot
				    "141.06.09-28610" : "6490.en-de-es-it-fr.141.06.09-28610.120308002013.cvc", #//2014-08-25 drohr: auslastungsfix
				    "141.06.09-28621" : "6490.en-de.141.06.09-28621.120308002013.cvc",   #//2014-08-28 drohr: neue fw mit wlan gui fix
				    "141.06.09" 	  : "6490.en-de.141.06.09.120308002013.cvc",      #   //2014-08-29 drohr: neu offizielle fw auf basis der -28621
				    "141.06.10-28643" : "6490.en-de.141.06.10-28643.120308002013.cvc",	#//4.9.2014; drohr: bugfix release wegen freeze
				    "141.06.10-28654" : "6490.en-de.141.06.10-28654.120308002013.cvc",	#//4.9.2014; drohr: newest bugfix for freeze
				    "141.06.10"		  :	"6490.en-de.141.06.10.120308002013.cvc",  # 		//5.9.2014; drohr: neue offizielle version
				    "141.06.11-29083" : "6490.en-de.141.06.11-29083.120308002013.cvc",	#//14.10.2014; drohr: eng drop fuer jira issues
				    "141.06.11-29328" : "6490.141.06.11-29328.120308002013.cvc", 	#	//05.11.2014; drohr: eng drop bandbreiten issue
				    "141.06.11-29426" : "6490.141.06.11-29426.120308002013.cvc",	#		//14.11.2014; drohr: labor fw fuer Bandbreitenfix
				    "141.06.11-29485" : "6490.141.06.11-29485.120308002013.cvc",	#		//24.11.2014; drohr: udp issue fix
				    "141.06.11-29541" : "6490.en-de.141.06.11-29541.120308002013.cvc",	#	//04.12.2014; drohr: Homespot und udp fix
				    "141.06.21" 	  :	"6490.en-de.141.06.21.120308002013.cvc",	#			//18.12.2014; drohr: neue offizielle version
				    "141.06.22-29826" : "6490.141.06.22-29826.120308002013.cvc",		#	//22.01.2015; drohr: Eng Drop mit Jira Fix fuer 116,120,115,111,74
				    "141.06.22" 	  :	"6490.en-de.141.06.22.120308002013.cvc"		#	//02.02.2015; drohr: neue Release FW
				
}

TC7200K = {
				    "STD2.49.02" : "tc7200k-d2.49.02-121222-f-101.bin",
				    "STD2.49.04" : "tc7200k-d2.49.04-130206-f-101.bin",
				    "STD2.49.05" : "TC7200K-D2.49.05-130207-F-101.bin",
				    "STD2.49.06" : "TC7200K-D2.49.06-130226-F-101.bin",
				    "STD2.49.07" : "TC7200K-D2.49.07-130311-F-101-e.img",
				    "STD2.49.08" : "TC7200K-D2.49.08-130313-F-101-e.img",
				    "STD2.49.09" : "TC7200K-D2.49.09-130402-F-101-e.img",
				    "STD2.49.11" : "TC7200K-D2.49.11-130521-F-101-E.img",
				    "STD2.49.12.T7" : "TC7200K-D2.49.12.T7-130808-F-101.bin",
				    "STD2.49.13.T3" : "TC7200K-D2.49.13.T3-130725-F-101.bin",
				    "STD2.49.13.T6" : "tc7200k-d2.49.13.t6-130913-f-101.bin",
				    "STD2.49.13.T8" : "TC7200K-D2.49.13.T8-131001-F-101.bin",
				    "STD2.49.13.T9" : "TC7200K-D2.49.13.T9-131031-F-101.bin",
				    "STD2.49.13.T10" : "TC7200K-D2.49.13.T10-131108-F-101.bin",
				    "STD2.49.13.T11" : "TC7200K-D2.49.13.T11-131119-F-101.bin",
				    "STD2.49.13.T13" : "TC7200K-D2.49.13.T13-131128-F-101.bin",
				    "STD2.49.13.T14" : "TC7200K-D2.49.13.T14-131128-F-101.bin",
				    "STD2.49.13.T15" : "TC7200K-D2.49.13.T15-131204-F-101.bin",
				    "STD2.49.13.T16" : "tc7200k-d2.49.13.t16-131206-f-101.bin",
				    "STD2.49.13.T17" : "tc7200k-d2.49.13.t17-131211-f-101.bin",
				    "STD2.49.13.T19" : "TC7200K-D2.49.13.T19-131219-F-101.bin",
				    "STD2.49.13.T20" : "TC7200K-D2.49.13.T20-131220-F-101.bin",
				    "STD2.49.13.T21" : "TC7200K-D2.49.13.T21-131220-F-101.bin",
				    "STD2.49.13.T22" : "TC7200K-D2.49.13.T22-140102-F-101.bin",
				    "STD2.49.13.T23" : "TC7200K-D2.49.13.T23-140108-F-101.bin",
				    "STD2.49.13.T24" : "TC7200K-D2.49.13.T24-140114-F-101.bin",
				    "STD2.49.13.T25" : "TC7200K-D2.49.13.T25-140114-F-101.bin",
				    "STD2.49.13.T27" : "TC7200K-D2.49.13.T27-140116-F-101.bin",
				    "STD2.49.13" : "TC7200K-D2.49.13-140116-F-101-E.img",
				    "STD2.49.14.T1" : "TC7200K-D2.49.14.T1-140122-F-101.bin",
				    "STD2.49.14.T2" : "TC7200K-D2.49.14.T2-140127-F-101.bin",
				    "STD2.49.14" : "TC7200K-D2.49.14-140127-F-101-E.img",
				    "STD2.49.15.T1" : "tc7200k-d2.49.15.t1-140211-f-101.bin",
				    "STD2.49.15.T2" : "TC7200K-D2.49.15.T2-140224-F-101.bin",
				    "STD2.49.15" : "TC7200K-D2.49.15-140224-F-101-E.img",
				    "BFC5510mp1" : "BRCM_BFC5510mp1_KDG_DsLite_TPTest.bin",
				    "STD2.49.16.T1" : "TC7200K-D2.49.16.T1-140304-F-101-E.img",
				    "STD2.49.16" : "tc7200k-d2.49.16-140304-f-101-e.img",
				    "STD2.49.17" : "TC7200K-D2.49.17-140812-F-101-E.img",
				    "STD2.49.17.T2" : "TC7200K-D2.49.17.T2-140331-F-101.bin",
				    "STD2.49.17.T3" : "TC7200K-D2.49.17.T3-140806-F-101.bin",
				    "STD2.49.17.T4" :"TC7200K-D2.49.17.T4-140808-F-101.bin",
				    "STD2.49.20" : "TC7200K-D2.49.20-140416-F-101-E.img",
				    "STD2.49.20.T1" : "TC7200K-D2.49.20.T1-140401-F-101-E.img",
				    "STD2.49.20.T2" : "TC7200K-D2.49.20.T2-140416-F-101-E.img",
				    "STD2.49.21.T1" : "TC7200K-D2.49.21.T1-140508-F-101-E.img",
				    "STD2.49.21.T2" : "tc7200k-d2.49.21.t2-140514-f-101.bin",
				    "STD2.49.21.T4" : "TC7200K-D2.49.21.T4-140609-F-101.bin",
				    "STD2.49.21.T5" : "TC7200K-D2.49.21.T5-140619-F-101.bin",
				    "STD2.49.21.T6" : "TC7200K-D2.49.21.T6-140701-F-101.bin",
				    "STD2.49.21.T7" : "TC7200K-D2.49.21.T7-140715-F-101.bin",
				    "STD2.49.21.T8" : "TC7200K-D2.49.21.T8-140812-F-101-E.img",
				    "STD2.49.21.T9" : "TC7200K-D2.49.21.T9-140821-F-101-E.img",
				    "STD2.49.21" : "TC7200K-D2.49.21-140821-F-101-E.img",
				    "STD2.49.22.T1" : "TC7200K-D2.49.22.T1-140903-F-101.bin",
				    "STD2.49.23" : "TC7200K-D2.49.23-141028-F-101-E.img",
				    "STD2.49.24.T1" : "TC7200K-D2.49.24.T1-141029-F-101.bin",
				    "STD2.49.24.T3" : "TC7200K-D2.49.24.T3-150407-F-101.bin",
				    "STD2.49.24.T4" : "TC7200K-D2.49.24.T4-150408-F-101.bin",
				    "STD2.49.24.T5" : "TC7200K-D2.49.24.T5-150409-F-101.bin",
				    "STD2.49.24.T6" : "TC7200K-D2.49.24.T6-150416-F-101.bin"
				    }
TC720020 = {

}

##########technicolor##############
##########Hitron###################

##########AVM######################
FritzBox6360 = {}