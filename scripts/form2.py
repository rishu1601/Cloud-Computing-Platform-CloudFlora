#!/usr/bin/python2
import cgi
import commands

print "Content-Type: text/html"
print

ip=cgi.FormContent()["IP"][0]
pas=cgi.FormContent()["password"][0]
rpm=cgi.FormContent()["rpm"][0]
status=commands.getstatusoutput("sshpass -p {} ssh -o stricthostkeychecking=no -l root {} yum install {} -y".format(pas,ip,rpm))
if status[0]==0:
	print "Software installed successfuly"
else:
	print "Software cannot be installed"
