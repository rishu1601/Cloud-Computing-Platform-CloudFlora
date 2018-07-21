#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html"
cont_name=cgi.FormContent()['x'][0]
cont_start_status=commands.getstatusoutput("sudo docker start {0}".format(cont_name))

if cont_start_status[0]==0:
	print "location: docker_manage.py"
	print
else:
	print
	print"""
	<script>
		function lw()
		{
			alert("Container Cannot be Started")
			document.location='docker_manage.py'
			}
	lw()	
	</script>
	"""
