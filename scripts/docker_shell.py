#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html"
cont_name=cgi.FormContent()['x'][0]
print "Set-Cookie:cntnr_nm={}".format(cont_name)
print "location: ../docker_shell.html"
print

