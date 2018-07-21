#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html"
print
print """
<script>
function os_start(os_name)
{
	document.location='os_start.py?x=' + os_name;
}
function os_stop(os_name)
{
	document.location='os_stop.py?x=' + os_name;
}
function os_remove(os_name)
{

	document.location='os_remove.py?x=' + os_name;
}
</script>
"""
caas_server_password="redhat"
caas_server_ip="192.168.43.240"
z=0

print "<div style='background-color:PowderBlue' align='center'><br/><br/><a href='../iaas.html'>Go Back</a><h1>OS MANAGEMENT PORTAL</h1><hr><table border='5' cellpadding=5px><th>OS NAME</th><th>Status</th><th>Start</th><th>Stop</th><th>Remove</th>"
for i in commands.getoutput('sshpass -p {} ssh -o stricthostkeychecking=no -l root {} virsh list --all'.format(caas_server_password,caas_server_ip)).split('\n'):
	if z<=1:
		z+=1
		pass
	else:
		j=i.split()
		print "<tr><td>" + j[1] + "</td><td>" + j[-1] + "</td><td><input value='" + j[1] + "'type='button' onclick=os_start(this.value) /> " + "</td><td><input value='" + j[1] + "'type='button' onclick=os_stop(this.value) />" + "</td><td><input value='" + j[1] + "'type='button' onclick=os_remove(this.value) />" + "</td></tr>"

print "</table></div><br/>"
