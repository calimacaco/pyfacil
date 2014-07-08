from pysnmp.entity.rfc3413.oneliner import cmdgen

dirip='13.179.61.70'

errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
  cmdgen.CommunityData('my-agent', 'public', 0),
  #estandar cups
  cmdgen.UdpTransportTarget((dirip, 161)),(1,3,6,1,2,1,43,10,2,1,4,1,1))
print varBinds
for i in range(1,1400):
	errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
	  cmdgen.CommunityData('my-agent', 'public', 0),
	  #estandar kyocera km
	  cmdgen.UdpTransportTarget((dirip, 161)),(1,3,6,1,2,1,43,10,2,1,4,1,i))
	print varBinds
