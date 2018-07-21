#!/usr/bin/python2
print "Content-Type: text/html"
print
import cgi
import Cookie
import os
import commands
image_name=cgi.FormContent()['save'][0]
retrieve_cookies=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
cname=retrieve_cookies['container_name'].value
print "<body style='background-color:PowderBlue;'><div align='center' valign='top' id='newdocker'>"
save_status=commands.getstatusoutput("sudo docker commit {0} {1}".format(cname,image_name))
if save_status[0]==0:
	print "<h3>Docker image {} from container {} saved successfuly</h3>".format(image_name,cname)
	print "</h4><hr /><a href='docker_manage.py'>Docker Management</a><br/><a href='caas.py'>CAAS Home</a></div></body>"
else:
	print "<script>\nfunction back(){alert('could not SAVE IMAGE')\ndocument.location='caas.py'}back()</script>"

