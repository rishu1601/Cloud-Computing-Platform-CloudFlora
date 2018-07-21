#!/usr/bin/python2
import cgi,cgitb
import commands

print "content-type: text/html"
print 
s1="1"
s2="1"
s3="1"
s4="1"
s5="1"
s6="1"
form=cgi.FieldStorage()
image_name=cgi.FormContent()['image_name'][0]
version=cgi.FormContent()['version'][0]
ImageName="centos:latest"
if form.getvalue('ssh-server'):
		s1="ssh-server"
if form.getvalue('ssh-client'):
		s2="ssh-client"
if form.getvalue('httpd'):
		s3="httpd"
if form.getvalue('net-tools'):
		s4="net-tools"
if form.getvalue('python2'):
		s5="python2"
if form.getvalue('nfs'):
		s6="nfs"
commands.getstatusoutput("sudo touch /commit/Dockerfile")
commands.getstatusoutput("sudo chown apache /commit/Dockerfile")
commands.getstatusoutput("echo 'FROM centos:latest' | sudo cat >> /commit/Dockerfile")
if s1 == "ssh-server":
   commands.getoutput("echo 'RUN yum install openssh-server -y' | sudo cat >> /commit/Dockerfile")
if s2 == "ssh-client":
   commands.getoutput("echo 'RUN yum install openssh-client -y' | sudo cat >> /commit/Dockerfile")
if s3 == "httpd":
   commands.getoutput("echo 'RUN yum install httpd -y' |sudo cat >> /commit/Dockerfile")
if s4 == "net-tools":
   commands.getoutput("echo 'RUN yum install net-tools -y' |sudo cat >> /commit/Dockerfile")
if s5 == "python2":
   commands.getstatusoutput("echo 'RUN yum install python2 -y' | sudo cat >> /commit/Dockerfile")
if s6 == "nfs":
   commands.getstatusoutput("echo 'RUN yum install nfs-utils -y' | sudo cat >> /commit/Dockerfile")

commands.getstatusoutput("sudo docker build -t {0}:{1} /commit".format(image_name,version))
f=open('/commit/Dockerfile','w')
a=""
f.append(a)
f.close()
print commands.getstatusoutput("sudo docker images {0}:{1}".format(image_name,version))
if commands.getstatusoutput[0]==0:
	print "<br/>"
	print "<a href='caas.py'>Click Here and Get your Image</a>"

