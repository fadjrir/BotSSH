#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.server import *
import os

__banner__ = m +"""
  ___      _   ___ ___ _  _ """ + k + """ 
 | _ ) ___| |_/ __/ __| || |  #dev by Fadjri_ """ + g + """ 
 | _ \/ _ \  _\__ \__ \ __ | """ + b + """ 
 |___/\___/\__|___/___/_||_| """ + m + """ 
   BotSSH Free Account SSH 
""" + w

__list_server__ = g + """
 *""" + w + """ Select Secure Shell Server 

""" + w + """ [""" + m + """1""" + w + """] SSH Server 1 United States
""" + w + """ [""" + k + """2""" + w + """] SSH Server 2 United States
""" + w + """ [""" + g + """3""" + w + """] SSH Server 3 United States
""" + w + """ [""" + b + """4""" + w + """] SSH Server 1 Singapore GS
""" + w + """ [""" + m + """5""" + w + """] SSH Server 2 Singapore GS
""" + w + """ [""" + k + """6""" + w + """] SSH Server 3 Singapore GS
"""

def create():
    os.system("clear")
    print(__banner__ + __list_server__)
    try:
        choice = str(input(b + ">" + w + " Choice Server" + g + ": " + w))
        if (choice == "1"):
            host = "us-1.myssh.info"
            referer = "usa1.php"
            ip = "45.32.220.233"
            ngebot(referer, host, ip)
            pass
        elif (choice == "2"):
            host = "us-2.myssh.info"
            referer = "usa2.php"
            ip = "149.28.136.138"
            ngebot(referer, host, ip)
            pass
        elif (choice == "3"):
            host = "us-3.myssh.info"
            referer = "usa3.php"
            ip = "207.148.119.190"
            ngebot(referer, host, ip)
            pass
        elif (choice == "4"):
            host = "sg-1.createssh.com"
            referer = "sggs1.php"
            ip = "162.246.19.251"
            ngebot(referer, host, ip)
            pass
        elif (choice == "5"):
            host = "sg-2.createssh.com"
            referer = "sggs2.php"
            ip = "162.246.19.251"
            ngebot(referer, host, ip)
            pass
        elif (choice == "6"):
            host = "sg-3.createssh.com"
            referer = "sggs3.php"
            ip = "162.246.19.251"
            ngebot(referer, host, ip)
            pass

        else:
            create()
            return
        pass
    except KeyboardInterrupt:
        sys.exit(1)
        pass
    pass

if __name__ == "__main__":
    create()
    pass
