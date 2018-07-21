#!/usr/bin/python2
import cgi 
import commands
print "Content-Type: text/html"
username=cgi.FormContent()['user'][0]
fh=open('/content/.user_info.txt','r')
lines=[i.rstrip() for i in fh.readlines()]
userinfo=[i.split(" ") for i in lines]
l=len(userinfo)
i=0
while i<l:
	if username==userinfo[i][0]:	
		print "location: ../temp.html"
	i=i+1

