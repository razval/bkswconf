#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""created by razval@xakep.ru"""

import os
import time
from subprocess import Popen
import telnetlib
import time
from datetime import datetime, timedelta, date, time as dt_time

#constants
USER = "root"
PASS = "toor"
SUBNET = "192.168.111." 
IPSRVBUP = "192.168.111.52"
DATE = datetime.today()

#functions
def connect(tn):
	tn = telnetlib.Telnet(ip)
	tn.write(USER + "\n")
	tn.write(PASS + "\n")	
#	tn.read_until(while s!=: read)
	while tn.write:
		try:
			tn.write("upload configuration " + str(IPSRVBUP) +\
				" " + str(ip) + "-" +\
				str(DATE.strftime('%d.%m.%y-%H.%M')) + "\n")
		except:
			tn.write("upload cfg_toTFTP " + str(IPSRVBUP) +\
				" " + str(ip) + "-" +\
				str(DATE.strftime('%d.%m.%y-%H.%M')) + "\n")
	tn.read_until("Success")
	tn.write("logout\n")
	print ('%s SV_C' % ip)				

#########
devnull = open(os.devnull, 'wb')
p=[]
for n in range (1, 255):
	ip=SUBNET + "%d" %n
	p.append((ip, Popen(['ping', '-n', '-c', '1', '-s' '0',\
		'-i', '0.2', '-W', '1', ip], stdout=devnull)))
while p:
	for i, (ip, proc) in enumerate(p[:]):
		if proc.poll() is not None:
			p.remove((ip, proc))
			if  proc.returncode == 0:
				print ('%s OK' % ip)
				try:	
					connect(ip)
				except:
					print ('%s ER_C' % ip)			
			elif proc.returncode == 2:
				print ('% NOT RESPOND' % ip)
			else:
				pass #print ('%s FAIL' % ip)
	time.sleep(.04)
devnull.close()
