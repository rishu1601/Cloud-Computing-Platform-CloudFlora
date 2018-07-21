#!/usr/bin/python2
import cgi
print "content-type: text/html"
userName = cgi.FormContent()['username'][0]
passWord = cgi.FormContent()['password'][0]
fh=open('/content/.user_info.txt','r')
lines=[i.rstrip() for i in fh.readlines()]
userinfo=[i.split(" ") for i in lines]
fh.close()
cust_name=""
l=len(userinfo)
i=0
while i<l:
	if username==userinfo[i][0] and password==userinfo[i][1]:
		cust_name=userinfo[i][2] + userinfo[i][3]
		l="Set-Cookie:usn={};\r\n".format(userinfo[i][0])
		m="Set-Cookie:p={};\r\n".format(userinfo[i][1])
		n="Set-Cookie:usn={};\r\n".format(cust_name)
		print "location ../form_services.html"
		print
else:
	print "location ../login.html"
	print
