#!/usr/bin/python2
import cgi
import commands
import docker_list
import os
import Cookie
print "Content-Type: text/html"
t=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
cont_count=t['cont_count'].value
print
i=0
image_name=[]
cont_name=[]
while i<int(cont_count):
	cont=cgi.FormContent()['cont_nm{}'.format(i)][0]
	img=cgi.FormContent()['image_name{}'.format(i)][0]
	image_name.append(img)
	cont_name.append(cont)
	i=i+1
i=0
print "<div align='left'><h3>Container Launch Status</h3>"
while i<int(cont_count):
	j=i+1
	docker_name_exists= commands.getstatusoutput("sudo docker inspect {0}".format(cont_name[i]))
	if docker_name_exists[0]==0:
		print "Container {} : {} already exists".format(j,cont_name[i])
	else:
		commands.getoutput("sudo docker run  -dit --name {0}  {1}".format(cont_name[i],image_name[i]))
		print "Container {} : {} launched from image {}".format(j,cont_name[i],image_name[i])
	print "<br/>"	
	i=i+1 
print "<a href='docker_manage.py'>Click here to manage all containers</a>   <a href='caas.py'>Click here to go to main page of CAAS</div>"
