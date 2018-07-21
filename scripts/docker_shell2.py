#!/usr/bin/python2
print "Content-Type: text/html"
print
import cgi
import Cookie
import os
import commands

command=cgi.FormContent()['code'][0]
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
cname=t['cntnr_nm'].value
print "<div align='center'  valign='top' id='newdocker'>"
print "<h4><i>The container " + cname +  " produced the following output</i></h4>"
command_run_status=commands.getstatusoutput("sudo docker exec {0} {1}".format(cname,command))
if command_run_status[0]==0:
	print "<pre>"
	print command_run_status[1]
	print "</pre><hr /><a href='docker_manage.py'>Click here to go back</a></div>"
	
else:
	print "<script>\nfunction back(){alert('could not run command')\ndocument.location='caas.py'}back()</script>"
	
