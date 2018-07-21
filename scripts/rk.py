#!/usr/bin/python2
import cgi
import commands
ip=raw_input("Enter ip : ")
password=raw_input("Enter password : ")
soft=raw_input("Enter soft : ")

hosts="""
[web]\n
{} ansible_ssh_user=root ansible_ssh_pass={}\n
""".format(ip,password)
f=open('../ansible/hosts.txt','w')
f.write(hosts + "\n")
f.close()
fh=open('../ansible/web.yml','w')
installpackage="""---
- hosts: web
  tasks:
   - package:
         name: "{0}"
         use: yum
   - copy:
         src: "/web/index.html"
         dest: "/webcontent"
   - service:
         name: "{0}"
         state: restarted
""".format(soft)
fh.write(installpackage)
fh.close()
print commands.getstatusoutput("sudo ansible-playbook -i ../ansible/hosts.txt ../ansible/web.yml")
