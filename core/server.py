#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
import urllib3
import requests
import sys

g = "\033[32;1m"
w = "\033[0m"
b = "\033[36;1m"
m = "\033[31;1m"
k = "\033[33;1m"

def ngebot(referer, host, ip):
    headers = {
        "Host": "myssh.info",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:69.0) Gecko/20100101 Firefox/69.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "53",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "http://myssh.info/servers/" + referer,
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    BASE_PATH_URL = "https://myssh.info/servers/new/create/index.php"
    r = requests.Session()
    urllib3.disable_warnings()
    try:
        print("\nInsert your Username and Password")
        username = str(input(b + ">" + w + " Username" + g + ": " + w))
        if (username == ""):
            sys.exit(1)
            pass
        else:
            pass
        password = str(input(b + ">" + w + " Password" + g + ": " + w))
        if (password == ""):
            sys.exit(1)
            pass
        else:
            pass
        data = {
            "username": username, "password": password, "type": "4", "code": "kshfree"
        }
        print("Process: Creating your account SSH at username '"+ g + username + w + "' & password '" + g + password + w + "' ...")
        try:
            regx = r.post(BASE_PATH_URL, data=data, timeout=30, verify=False)
            date_after_month = datetime.now() + relativedelta(days=6)
            if (regx.status_code == 200):
                print("\nResult: '" + g + "SSH Account Successfull Created!" + w + "'")
                print("Server Status: " + g + "connected" + w)
                print(m + " -" + w + " Host to IP" + g + ": " + w + host + "/" + ip)
                print(k + " -" + w + " Username" + g + ":" + w + " myssh.info-" + username)
                print(g + " -" + w + " Password" + g + ":" + w + " myssh.info-" + password)
                print(b + " -" + w + " Dropbear" + g + ":" + w + " Port 443")
                print(m + " -" + w + " OpenSSH" + g + ":" + w + " Port 22")
                print(k + " -" + w + " Expired Date" + g + ": " + w +
                      date_after_month.strftime('%d-%m-%Y'))
                print()
                return
            else:
                sys.exit(1)
                pass
        except requests.exceptions.ReadTimeout:
            print("\n[" + m + "!" + w + "]" + k + " WARNING" + w + ": Read Timeout at server ...")
            pass
        except requests.exceptions.ConnectionError:
            print("\n[" + m + "!" + w + "]" + k + " WARNING" +
                  w + ": Max retries exceeded with server ...")
            pass
        except requests.exceptions.ConnectTimeout:
            print("\n[" + m + "!" + w + "]" + k + " WARNING" +
                  w + ": Connection Timeout ...")
            pass
        # soup = BeautifulSoup(regx.text, 'html.parser')
        # print(soup.text)
        pass
    except KeyboardInterrupt:
        sys.exit(1)
        pass
    pass
