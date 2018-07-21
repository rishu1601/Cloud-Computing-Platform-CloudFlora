#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html" 


xi=commands.getstatusoutput("sudo docker stop rishabh")
if (xi[0]==0):
	print "location: ../form_service.html"
	print
else :
	print
	print "<pre>Sorry..failed to close the container</pre>"
	print "<a href='caas.py'>Click here to go back to Cantainer Launcher</a>"
