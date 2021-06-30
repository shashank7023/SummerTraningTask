#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess 
import cgi
import time



data = cgi.FieldStorage()

cmd = data.getvalue("command")

out = subprocess.getoutput("sudo " +cmd+ " --kubeconfig /root/kubews/admin.conf") 

print(out)
