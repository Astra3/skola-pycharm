#!/usr/bin/python3

import cgi
import cgitb
from subprocess import Popen, PIPE


def field_check():
    if "ip" not in args:
        print("Je potřeba zadat proměnnou 'ip' jako string přes GET\n"
              "Další možné proměnné:\n"
              "c - počet pingů (výchozí 4)\n"
              "i - interval mezi pingy (výchozí 1s)\n".replace("\n", "<br>"))
        exit(0)
    return ping(args.getvalue("ip"))


def ping(ip: str):
    if "c" in args:
        count = args.getvalue("c")
    else:
        count = 4
    if "i" in args:
        interval = args.getvalue("i")
    else:
        interval = 1
    ping_proc = Popen(["ping", "-c", str(count), "-i", str(interval), str(ip)], stdout=PIPE, stderr=PIPE)
    return ping_proc


print("Content-Type: text/html\n\n")
print("<html lang='cs'><head><meta charset='UTF-8'><title>Ping</title></head></html>")
cgitb.enable()
args = cgi.FieldStorage()
a = field_check()
a.wait()
stdout = a.stdout.readlines()
stderr = a.stderr.readlines()
for i in stdout:
    print(i.decode().replace("\n", "<br>"))
try:
    if b', 0%' in stdout[-2]:
        print("<br><b style='color: green'>PING DOKONČEN ÚSPĚŠNĚ</b>")
    else:
        print("<br><b style='color: red'>PING ZAZNAMENAL ZTRÁTY</b>")
except IndexError:
    for i in stderr:
        print(i.decode().replace("\n", "<br>"))
    print("<br><b style='color: red'>PING SELHAL</b>")
