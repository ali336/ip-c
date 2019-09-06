import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests

#-Animasi-#
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00.1)

def cek():
	os.system('reset')
	jalan("[*] Getting Your IP....")
	time.sleep(1)
	anj=requests.get("https://api.myip.com")
	b = json.loads(anj.text)
	print("[*] Your IP : ") +b['ip']
	print("[*] Country : ") +b['country']
	
cek()