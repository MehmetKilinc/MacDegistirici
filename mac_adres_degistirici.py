import subprocess
import optparse
import re


def kullanici_girdisi():

	nesne = optparse.OptionParser()
	nesne.add_option("-a" , "--arayuz" , dest = "arayuz" , help = "arayuz bilgisi girilir.")
	nesne.add_option("-m" , "--mac" , dest = "mac_adres" , help = "mac adres bilgisi girilir.")
	return nesne.parse_args()



def mac_adres_degistirici(arayuz , mac_adres):

	subprocess.call(["ifconfig" , arayuz , "down"])
	subprocess.call(["ifconfig" , arayuz , "hw" , "ether" , mac_adres])
	subprocess.call(["ifconfig" , arayuz , "up"])
	
def mac_adres_kontrol(arayuz):

	ifconfig = subprocess.check_output(["ifconfig" , arayuz])
	yeni_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig)
	
	if yeni_mac:
		return yeni_mac.group(0)
	else:
		return None
	
	
(kullanici_girdileri , argumantlar) = kullanici_girdisi()

arayuz = kullanici_girdileri.arayuz
mac_adres = kullanici_girdileri.mac_adres
mac_adres_degistirici(arayuz , mac_adres)
yeni_mac = mac_adres_kontrol(arayuz)

subprocess.call(["figlet" , "mac" , "degistirici"])

if yeni_mac == mac_adres:
	print("islem basarili")
	
else:
	print("islem basarisiz")


