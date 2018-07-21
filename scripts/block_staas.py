#!/usr/bin/python2

import cgi
import commands


print"content-type: text/html"
print


ip="192.168.43.149"
password="redhat"
username=cgi.FormContent()['username'][0]
clip=cgi.FormContent()['clip'][0]
clpassword=cgi.FormContent()['clpassword'][0]
size=cgi.FormContent()['size'][0]
#print cgi.FormContent()




#step 1:- Make a lv partition format 

s=commands.getstatusoutput("sshpass -p {2} ssh -o stricthostkeychecking=no -l root {1}  mkdir /{0}".format(username,ip,password))

st=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} lvcreate --size {2}G --name {3} myvg".format(password,ip,size,username))


commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount /dev/myvg/{2} /{2}".format(password,ip,username))

commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} yum install scsi-targets-utils -y".format(password,ip,username))




#step 2:- configure vim /etc/tgt/

commands.getstatusoutput("sudo chown apache /mnt")
commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/tgt/targets.conf  /mnt/".format(password,ip))
fh=open("/mnt/targets.conf",'a')
target="\n<target /{0}>\n backing-store /dev/myvg/{0}\n</target>".format(username)
fh.write(target)
fh.close()

commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /mnt/targets.conf root@{1}:/etc/tgt/".format(password,ip))






#step 3:- service start
commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl restart tgtd".format(password,ip))




#step 4:-client side mounting of block storage

iscsidis=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} iscsiadm --mode discoverydb --type sendtargets  --portal {2}:3260  --discover".format(clpassword,clip,ip))
if iscsidis[0]==0:
	print "<h2>Block-Storage Discovered</h2>"
else:
	print "<h2>Sorry Block Storage could not be discovered</h2>"
	print "<a href='../block_staas.html'>Go Back</a>"

iscsilogin=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} iscsiadm --mode node  --targetname /{2}  --portal {3}:3260  --login".format(clpassword,clip,username,ip))

if iscsilogin[0]==0:
        print "<h2>Requested Block-Storage Added Successfully</h2>"
	print "<pre>The drive size is : {}<pre>".format(size)
	print "<a href='../block_staas.html'>Go Back</a>"
else:
        print "<h2>Sorry Block Storage could not be discovered</h2>"
	print "<a href='../block_staas.html'>Go Back</a>"



