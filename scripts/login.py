#!/usr/bin/python2
import cgi
print "content-type: text/html"
userName = cgi.FormContent()['username'][0]
passWord = cgi.FormContent()['password'][0]
fh=open('/content/.user_info.txt','r')
lines=[i.rstrip() for i in fh.readlines()]
userinfo=[i.split(" ") for i in lines]
fh.close()
l=len(userinfo)
i=0
while i<l:
	if userName==userinfo[i][0] and passWord==userinfo[i][1]:
		print "Set-Cookie:usn={}".format(userinfo[i][0])
		print "Set-Cookie:p={}".format(userinfo[i][1])
		print "Set-Cookie:cnm={}".format(userinfo[i][2])
		print "location: ../user.html"
		print	
	i=i+1
print "location: ../index.html"
print
