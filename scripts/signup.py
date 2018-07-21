#!/usr/bin/python2
import cgi,cgitb
import commands
print "Content-Type: text/html"
username=cgi.FormContent()['user'][0]
fh=open('/content/.user_info.txt','r')
lines=[i.rstrip() for i in fh.readlines()]
userinfo=[i.split(" ") for i in lines]
fh.close()
l=len(userinfo)
i=0
while i<l:
	if username==userinfo[i][0]:	
		print "location: ../signup.html"
		print
	i=i+1
password=cgi.FormContent()['pass'][0]
fname=cgi.FormContent()['fname'][0]
lname=cgi.FormContent()['lname'][0]
dob=cgi.FormContent()['dob'][0]
email=cgi.FormContent()['email'][0]
cn=cgi.FormContent()['cn'][0]
fk=open('/content/.user_info.txt','a')
newuser="{} {} {} {} {} {} {}".format(username,password,fname,lname,dob,email,cn)
fk.write(newuser + "\n")
fk.close()
print "location: ../home.html"
print
