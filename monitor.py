import os
import socket
import sqlite3
import time
from shadowsocks.web.mail import monitorup
from shadowsocks.web.mail import monitordown

def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(25)
    try:
        s.connect((ip,int(port)))
        return 1
    except:
        return 0
    s.close()

while True:
    cx = sqlite3.connect('/var/www/shadowsocks.net/shadowsocks.db')
    cu = cx.cursor()
    cu.execute("select * from web_Account")
    lists = cu.fetchall()
    list = []
    for a in lists:
        d = {}
        d['id'] = a[0]
        d['ip'] = a[1]
        d['port'] = a[2]
        d['is_on'] = a[13]
        d['mailto'] = a[7]
        list.append(d)
    for i in list:
        id = i['id']
        ip = i['ip']
        port = i['port']
        on = i['is_on']
        mailto = i['mailto']
        is_on = IsOpen(ip,port)
        sql = "update web_Account set is_on = %d where id = %d" % (is_on,id)
        cu.execute(sql)
        cx.commit()
        if on != is_on and is_on == 1:
            monitorup(mailto,ip)
        elif on != is_on and is_on == 0:
            monitordown(mailto,ip)
    cu.close()
    cx.close()
    time.sleep(60)
