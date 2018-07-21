#!/usr/bin/python2
print "content-type: text/html"
print
import cgi
import commands
#print cgi.FormContent()
cIP=cgi.FormContent()['cIP'][0]
cPassword=cgi.FormContent()['cpass'][0]
user=cgi.FormContent()['user'][0]
size=cgi.FormContent()['capacity'][0]
sIP="192.168.43.149"
sp="redhat"
