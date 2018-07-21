#!/usr/bin/python2
import cgi
import commands

print "Content-Type: text/html"
print

selection=cgi.FormContent()['type'][0]

