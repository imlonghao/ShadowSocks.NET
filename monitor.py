import os
import socket
import sqlite3

def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        return 1
    except:
        return 0

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
    list.append(d)

for i in list:
    id = i['id']
    ip = i['ip']
    port = i['port']
    is_on = IsOpen(ip,port)
    sql = "update web_Account set is_on = %d where id = %d" % (is_on,id)
    print sql
    cu.execute(sql)
    cx.commit()

cu.close()
cx.close()
