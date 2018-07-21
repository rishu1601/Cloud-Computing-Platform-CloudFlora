#!/usr/bin/python2
import cgi,cgitb
import commands 
print "content-type: text/html"
choice=cgi.FormContent()['ds'][0]
y=commands.getstatusoutput("sudo docker pull {}".format(choice))
if y[0]==0:
	print "location: caas.py"
	print
else:
	print
	print "<h1>Error in pulling image</h1>"
	print "<a href='caas.py'>Click here to go back</a>"

