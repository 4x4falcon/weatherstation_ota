help = """
 Commands available

c1() 		= showWifiConfig()	 	- show the ssid and password for the wifi connection
c2(<SSID>) 	= setWifiSSID(<SSID>)	 	- set the SSID for the wifi
c3(<Password>)	= setWifiPassword(<Password>)	- set the password for the wifi

"""

print (help)

import json

wifi_cfg_file = 'config/wifi_cfg.json'


try:
	from ws.main.term import *
except:
	print ("no ws term")
	pass



def showWifiConfig():
	global wifi_cfg_file

	wifi_cfg = None

	try:
	        with open(wifi_cfg_file) as cf:
	                wifi_cfg = json.load(cf)
	        print ("SSID: ", wifi_cfg['wifi']['ssid'])
	        print ("PW: ", wifi_cfg['wifi']['password'])

	except OSError:
                print ("No wifi config file at ", wifi_cfg_file)
	except Exception:
		print ("Error occured")

def setWifiSSID(SSID=None):

	global wifi_cfg_file

	if (SSID != None):
		wifi_cfg = None

		try:
		        with open(wifi_cfg_file) as cf:
		                wifi_cfg = json.load(cf)
		        print ("Current SSID: ", wifi_cfg['wifi']['ssid'])
			wifi_cfg['wifi']['ssid'] = SSID
			print ("New ssid: ", wifi_cfg['wifi']['ssid'])
			with open(wifi_cfg_file, 'w') as cf:
				json.dump(wifi_cfg, cf)
		except OSError:
	                print ("No wifi config file at ", wifi_cfg_file)
		except Exception:
			print ("Error occured")


	else:
		print ("Nothing to change")


def setWifiPassword(PW=None):

	global wifi_cfg_file

	if (PW != None):
		wifi_cfg = None

		try:
		        with open(wifi_cfg_file) as cf:
		                wifi_cfg = json.load(cf)
		        print ("Current Password: ", wifi_cfg['wifi']['password'])
			wifi_cfg['wifi']['password'] = PW
			print ("New password: ", wifi_cfg['wifi']['password'])
			with open(wifi_cfg_file, 'w') as cf:
				json.dump(wifi_cfg, cf)

		except OSError:
	                print ("No wifi config file at ", wifi_cfg_file)
		except Exception:
			print ("Error occured")



	else:
		print ("Nothing to change")


def c1():
	showWifiConfig()

def c2(SSID=None):
	setWifiSSID(SSID)

def c3(Password=None):
	setWifiPassword(Password)
