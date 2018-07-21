#!/usr/bin/python2
print "content-type: text/html"
print
import cgi
import commands
print "<body style='background-color:pink;'>"
#print cgi.FormContent()
cIP=cgi.FormContent()['cIP'][0]
cPassword=cgi.FormContent()['cpass'][0]
user=cgi.FormContent()['user'][0]
size=cgi.FormContent()['capacity'][0]
sIP="192.168.43.149"
sp="redhat"
vgstatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} vgdisplay myvg".format(sp,sIP))
#print vgstatus[0]
lvcreate=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} lvcreate --size {2}G --name {3} myvg".format(sp,sIP,size,user))
#print lvcreate[0]
formatted=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkfs.ext4 /dev/myvg/{2}".format(sp,sIP,user))
#print formatted[0]
commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir -p /share/{2}".format(sp,sIP,user))
fstabstr="/dev/myvg/{0} /share/{0} ext4 defaults 1 2".format(user)
commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo chown apache /mnt".format(sp,sIP))
commands.getoutput("sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/fstab /mnt/".format(sp,sIP))
fs=open('/mnt/fstab','a')
fs.write(fstabstr + "\n")
fs.close()
x=commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /mnt/fstab root@{1}:/etc/fstab".format(sp,sIP))
l=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount -a".format(sp,sIP))
#print l[0]
if l[0]!=0:
	print "FATAL ERROR..PLZ CONTACT CLOUD ADMIN"
commands.getoutput("sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/exports /mnt/".format(sp,sIP))
nfsfh=open('/mnt/exports','a')
shareLoc="/share/{0} {1}(rw,no_root_squash)".format(user,cIP)
nfsfh.write(shareLoc + "\n")
nfsfh.close()
commands.getoutput("sshpass -p {0} scp -o stricthostkeychecking=no /mnt/exports root@{1}:/etc/exports".format(sp,sIP))

o=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl restart nfs".format(sp,sIP))
#print o[0]
commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir /media/{2}".format(cPassword,cIP,user))
mounted=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount {2}:/share/{3} /media/{3}".format(cPassword,cIP,sIP,user))
if mounted[0]==0:
	print "<div align='center'><p>Drive has been properly mounted..Please Check the Client System</p>"
	print "<a href='../staas.html'>Object Storage Home Page</a></div>"
