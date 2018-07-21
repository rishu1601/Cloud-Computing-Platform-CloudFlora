import commands
def docker_table():
	z=1
	print "<table border='5' align='center'><th>Image</th><th>Version</th>"
	for i in commands.getoutput("sudo docker images").split('\n'):
		if z==1:
			z=z+1
			pass
		else:
			j=i.split()
			print "<tr><td>" + j[0] + "</td><td>" + j[1] + "</td></tr>"

def docker_option():
	z=1
	print "<select name=cName>"
	for i in commands.getoutput("sudo docker images").split('\n'):
		if z==1:
			z=z+1
			pass
		else:
			j=i.split()
			print "<option value='" + j[0] + ":" + j[1] + "'>" + j[0] + ":" + j[1] + "</option>"
	print "</select>"
