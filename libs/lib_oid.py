###########DOCSIS GLOBAL PART 
###########downstream Table###############

DownChannelFrequency = "1.3.6.1.2.1.10.127.1.1.1.1.2"
DownChannelWidth = "1.3.6.1.2.1.10.127.1.1.1.1.3"
DownChannelModulation = "1.3.6.1.2.1.10.127.1.1.1.1.4"
DownChannelInterleave = "1.3.6.1.2.1.10.127.1.1.1.1.5"
DownChannelPower = "1.3.6.1.2.1.10.127.1.1.1.1.6"
DownChannelAnnex = "1.3.6.1.2.1.10.127.1.1.1.1.7"
_DownChannelModulation = { 1:'unknown',2:'other',3:'qam64',4:'qam256' } 
_DownChannelInterleave = { 1:'unknown',2:'other',3:'taps8Increment16',4:'taps16Increment8', 
			 5:'taps32Increment4',6:'taps64Increment2',7:'taps128Increment1',8:'taps12Increment17' } 
_DownChannelAnnex = { 1:'unknown',2:'other',3:'annexA',4:'annexB',5:'annexC' } 
##########upstream Table 

UpChannelFrequency = "1.3.6.1.2.1.10.127.1.1.2.1.2"
UpChannelWidth = "1.3.6.1.2.1.10.127.1.1.2.1.3"
UpChannelModulationProfile = "1.3.6.1.2.1.10.127.1.1.2.1.4"
UpChannelSlotSize = "1.3.6.1.2.1.10.127.1.1.2.1.5"
UpChannelTxTimingOffset = "1.3.6.1.2.1.10.127.1.1.2.1.6"
UpChannelRangingBackoffStart = "1.3.6.1.2.1.10.127.1.1.2.1.7"
UpChannelRangingBackoffEnd = "1.3.6.1.2.1.10.127.1.1.2.1.8"
UpChannelTxBackoffStart = "1.3.6.1.2.1.10.127.1.1.2.1.9"
UpChannelTxBackoffEnd = "1.3.6.1.2.1.10.127.1.1.2.1.10"
UpChannelScdmaActiveCodes = "1.3.6.1.2.1.10.127.1.1.2.1.11"
UpChannelScdmaCodesPerSlot = "1.3.6.1.2.1.10.127.1.1.2.1.12"
UpChannelScdmaFrameSize = "1.3.6.1.2.1.10.127.1.1.2.1.13"
UpChannelScdmaHoppingSeed = "1.3.6.1.2.1.10.127.1.1.2.1.14"
UpChannelType = "1.3.6.1.2.1.10.127.1.1.2.1.15"
UpChannelCloneFrom = "1.3.6.1.2.1.10.127.1.1.2.1.16"
UpChannelUpdate = "1.3.6.1.2.1.10.127.1.1.2.1.17"
UpChannelStatus = "1.3.6.1.2.1.10.127.1.1.2.1.18"
_UpChannelModulationProfile = { 1:'unknown',2:'other',3:'qam64',4:'qam256' } 
#################signal quality

SQUnerroreds = "1.3.6.1.2.1.10.127.1.1.4.1.2"
SQCorrecteds = "1.3.6.1.2.1.10.127.1.1.4.1.3"
SQUncorrectables = "1.3.6.1.2.1.10.127.1.1.4.1.4"
SQSignalNoise = "1.3.6.1.2.1.10.127.1.1.4.1.5"
SQMicroreflections = "1.3.6.1.2.1.10.127.1.1.4.1.6"
SQEqualizationData = "1.3.6.1.2.1.10.127.1.1.4.1.7"

###################CM status tables
CmStatus = "1.3.6.1.2.1.10.127.1.2.2.1"
CmStatusValue = "1.3.6.1.2.1.10.127.1.2.2.1.1"
CmStatusCode = "1.3.6.1.2.1.10.127.1.2.2.1.2"
CmStatusTxPower = "1.3.6.1.2.1.10.127.1.2.2.1.3"
CmStatusResets = "1.3.6.1.2.1.10.127.1.2.2.1.4"
CmStatusLostSyncs = "1.3.6.1.2.1.10.127.1.2.2.1.5"
CmStatusInvalidMaps = "1.3.6.1.2.1.10.127.1.2.2.1.6"
CmStatusInvalidUcds = "1.3.6.1.2.1.10.127.1.2.2.1.7"
CmStatusInvalidRangingResponses = "1.3.6.1.2.1.10.127.1.2.2.1.8"
StatusInvalidRegistrationResponses = "1.3.6.1.2.1.10.127.1.2.2.1.9"
CmStatusT1Timeouts = "1.3.6.1.2.1.10.127.1.2.2.1.10"
CmStatusT2Timeouts = "1.3.6.1.2.1.10.127.1.2.2.1.11"
CmStatusT3Timeouts = "1.3.6.1.2.1.10.127.1.2.2.1.12"
CmStatusT4Timeouts = "1.3.6.1.2.1.10.127.1.2.2.1.13"
CmStatusRangingAborteds = "1.3.6.1.2.1.10.127.1.2.2.1.14"
CmStatusDocsisOperMode = "1.3.6.1.2.1.10.127.1.2.2.1.15"
CmStatusModulationType = "1.3.6.1.2.1.10.127.1.2.2.1.16"
_CmStatusValue = { 1:'other',2:'notReady',3:'notSynchronized',4:'phySynchronized',5:'usParametersAcquired',
		  6:'rangingComplete',7:'ipComplete',8:'todEstablished',9:'securityEstablished',
		  10:'paramTransferComplete',11:'registrationComplete',12:'operational',13:'accessDenied' } 

#################CM DEvice Base 

Role = "1.3.6.1.2.1.69.1.1.1.0"
DateTime = "1.3.6.1.2.1.69.1.1.2.0"
ResetNow = "1.3.6.1.2.1.69.1.1.3.0"
SerialNumber = "1.3.6.1.2.1.69.1.1.4.0"
STPControl = "1.3.6.1.2.1.69.1.1.5.0"
_Role = {1:'cm',2:'cmtsActive',3:'cmtsBackup'}
_STPControl = {1:'stEnabled',2:'noStFilterBpdu',3:' noStPassBpdu'} 


#################NM ACCESS
NmAccessIp = "1.3.6.1.2.1.69.1.2.1.2"
NmAccessIpMask = "1.3.6.1.2.1.69.1.2.1.3"
NmAccessCommunity = "1.3.6.1.2.1.69.1.2.1.4"
NmAccessControl = "1.3.6.1.2.1.69.1.2.1.5"
NmAccessInterfaces = "1.3.6.1.2.1.69.1.2.1.6"
NmAccessStatus = "1.3.6.1.2.1.69.1.2.1.7"
NmAccessTrapVersion = "1.3.6.1.2.1.69.1.2.1.8"
_NmAccessControl = {1:'none',2:'read',3:'readWrite',4:'roWithTraps',5:'rwWithTraps',6:'trapsOnly'} 

##################SW Software Server
SwStatus = "1.3.6.1.2.1.69.1.3"
SwServer = "1.3.6.1.2.1.69.1.3.1.0"
SwFilename = "1.3.6.1.2.1.69.1.3.2.0"
SwAdminStatus = "1.3.6.1.2.1.69.1.3.3.0"
SwOperStatus = "1.3.6.1.2.1.69.1.3.4.0"
SwCurrentVers = "1.3.6.1.2.1.69.1.3.5.0"
SwServerAddressType = "1.3.6.1.2.1.69.1.3.6.0"
SwServerAddress = "1.3.6.1.2.1.69.1.3.7.0"
SwServerTransportProtocol = "1.3.6.1.2.1.69.1.3.8.0"
_SwAdminStatus = {1:'upgradeFromMgt',2:'allowProvisioningUpgrade',3:'ignoreProvisioningUpgrade'} 
_SwOperStatus = {1:'inProgress',2:'completeFromProvisioning',3:'completeFromMgt',4:'failed',5:'other'} 
_SwServerTransportProtocol = {1:'tftp',2:'http'}
####################Server
ServerBootState = "1.3.6.1.2.1.69.1.4.1"
ServerDhcp = "1.3.6.1.2.1.69.1.4.2"
ServerTime = "1.3.6.1.2.1.69.1.4.3"
ServerTftp = "1.3.6.1.2.1.69.1.4.4"
ServerConfigFile = "1.3.6.1.2.1.69.1.4.5" 
_ServerBootState = {1:'operational',2:'disabled',3:'waitingForDhcpOffer',4:'waitingForDhcpResponse',
		    5:'waitingForTimeServer',6:'waitingForTftp',7:'refusedByCmts',8:'forwardingDenied',
		    9:'other',10:'unknown'} 

######################Event
Ev = "1.3.6.1.2.1.69.1.5"
EvControl = "1.3.6.1.2.1.69.1.5.1"   #######SET 1 TO RESET LOGS !!!!
EvSyslog = "1.3.6.1.2.1.69.1.5.2"
EvThrottleAdminStatus = "1.3.6.1.2.1.69.1.5.3"
EvThrottleInhibited = "1.3.6.1.2.1.69.1.5.4"
EvThrottleThreshold = "1.3.6.1.2.1.69.1.5.5"
EvThrottleInterval = "1.3.6.1.2.1.69.1.5.6"
EvReporting = "1.3.6.1.2.1.69.1.5.7.1.2"
EvFirstTime = "1.3.6.1.2.1.69.1.5.8.1.2"
EvLastTime = "1.3.6.1.2.1.69.1.5.8.1.3"
EvCounts = "1.3.6.1.2.1.69.1.5.8.1.4"
EvLevel = "1.3.6.1.2.1.69.1.5.8.1.5"
EvId = "1.3.6.1.2.1.69.1.5.8.1.6"
EvText = "1.3.6.1.2.1.69.1.5.8.1.7"
_EvControl = {1:'resetLog',2:'useDefaultReporting'} 
_EvThrottleAdminStatus = {1:'unconstrained',2:'maintainBelowThreshold',3:'stopAtThreshold',4:'inhibited'} 
_EvReporting = {0:'local',1:'traps',2:'syslog'} 
_EvLevel = {1:'emergency',2:'alert',3:'critical',4:'error',5:'warning',6:'notice',7:'information',8:'debug'} 
################# Filter
#FilterLLCUnmatchedAction
#FilterLLCIndex
#FilterLLCStatus
#FilterLLCIfIndex
#FilterLLCProtocolType
#FilterLLCProtocol
#FilterLLCMatches
#FilterIpDefault
################# CPE
CpeEnroll = "CpeEnroll"
CpeIpMax = "1.3.6.1.2.1.69.1.7.2"
CpeIp = "1.3.6.1.2.1.69.1.7.3.1.1"
CpeSource = "1.3.6.1.2.1.69.1.7.3.1.2"
CpeStatus = "1.3.6.1.2.1.69.1.7.3.1.3"

############################## VENDOR SPECIIC PART

_oid = "1.3.6.1.2.1.1.2.0"
_vendor = "1.3.6.1.2.1.1.4.0"
_model = "1.3.6.1.2.1.1.5.0"
_sysdescr = "1.3.6.1.2.1.1.1.0"

# Interface status
STAT_Router_admin="1.3.6.1.2.1.2.2.1.7.1"
STAT_Router_oper="1.3.6.1.2.1.2.2.1.8.1"
STAT_CM_admin="1.3.6.1.2.1.2.2.1.7.2"
STAT_CM_oper="1.3.6.1.2.1.2.2.1.8.2"
STAT_MTA_admin="1.3.6.1.2.1.2.2.1.7.16"
STAT_MTA_oper="1.3.6.1.2.1.2.2.1.8.16"
STAT_ETH_CPE_admin="1.3.6.1.2.1.2.2.1.7.20"
STAT_ETH_CPE_oper="1.3.6.1.2.1.2.2.1.8.20" 

########CH6640E###############
CH6640E_greif = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.2" #((tunnel ))
CH6640E_greip = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.4"
CH6640E_grename = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.5"
CH6640E_fqdn = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.11"
CH6640E_pckin = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.7"
CH6640E_pckout = "1.3.6.1.4.1.35604.1.19.52.1.1010.1.1.1.6"
CH6640E_ssid = "1.3.6.1.4.1.35604.1.19.51.1.5.4.1.14.1.3"
#CH6640E_ssid = "1.3.6.1.4.1.35604.1.19.51.1.5.4.1.14.1.3"

############MTA####################
box_CM_MAC = "1.3.6.1.2.1.2.2.2.1.6.2"
box_IF = "1.3.6.1.2.1.4.22.1.1"
box_MAC_IF = "1.3.6.1.2.1.4.22.1.2"
box_IP_IF = "1.3.6.1.2.1.4.22.1.3"
box_cm_mac1  = "1.3.6.1.2.1.4.22.1.3.1"
box_cm_ip1 = "1.3.6.1.2.1.4.22.1.2.1"
mta_country = "1.3.6.1.4.1.35604.1.200.9.12.0"
mta_l = "1.3.6.1.4.1.35604.1.200.2.54"
mta_2 = "1.3.6.1.4.1.35604.1.200.9.2"
mta_3 = "1.3.6.1.4.1.35604.1.200.13.1.7"
mta_4 = "1.3.6.1.4.1.35604.1.200.18.1"
mta_5 = "1.3.6.1.4.1.35604.1.200.18.2"
mta_6 = "1.3.6.1.4.1.35604.1.200.18.3"
mta_4491 = "1.3.6.1.4.1.4491"
mta_callhistory = "1.3.6.1.4.1.35604.1.200.17.1.1.2.1"
mta_tone_ncs = "1.3.6.1.4.1.7432.2.1.1.32"
mta_tone_ncs2 = "1.3.6.1.4.1.7432.2.1.1.33"
mta_tone_pc20 = "1.3.6.1.4.1.35604.1.200.18.12.1"
mta_tone2_pc20 = "1.3.6.1.4.1.35604.1.200.18.13.1"