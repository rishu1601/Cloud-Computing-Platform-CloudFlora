#!/usr/bin/python2
import cgi 
import commands
print "Content-Type: text/html"
print
block_storage_IP="192.168.43.149"
block_storage_Pass="redhat"
user=cgi.FormContent()['user'][0]
size=cgi.FormContent()['capacity'][0]
choice=cgi.FormContent()['choice'][0]
if choice=="extend":
	lv_extend_status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo lvextend --size +{2}G /dev/myvg/{3}".format(block_storage_Pass,block_storage_IP,size,user))
	if lv_extend_status[0]==0:
		print "<body style='background-color:pink'><h2> Your storage has been resized successfully</h2>"
	else :
		print "<h2>Sorry but we have problems on our servers</h2><a href='../staas.html>Click Here to go Back</a>"
	lv_format_status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo resize2fs /dev/myvg/{3}".format(block_storage_Pass,block_storage_IP,size,user))
	if lv_format_status[0]==0:
		print "<h2> Your storage has been formated successfully</h2>"
		print "<br/><br/><div align='center'><a href='../staas.html'>Click Here to go Back</a></div>"
	else :
		print "<h2>Sorry but we have problems on our servers</h2><a href='../staas.html>Click Here to go Back</a></body>"
