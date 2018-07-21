#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html"
caas_server_password="redhat"
caas_server_ip="192.168.43.240"
os_name=cgi.FormContent()['x'][0]
os_start_status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo virsh start {2}".format(caas_server_password,caas_server_ip,os_name))

if os_start_status[0]==0:
	print "location: iaas_manage.py"
	print
else:
	print
	print"""
	<script>
		function lw()
		{
			alert('OS Cannot be Started')
			document.location='iaas_manage.py'
			}
	lw()	
	</script>
	"""
