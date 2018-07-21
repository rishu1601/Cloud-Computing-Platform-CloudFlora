#!/usr/bin/python2
import commands
import cgi
print "Content-Type: text/html"
print
print"""
<script>
function back()
{
	document.location='../cloudflora.html'
}
function mantain()
{
	document.location='io2.py'
}
function save()
{
	alert('Present data saved in the desired location')
}
</script>
"""
f=open('/content/user1.txt','r').read()
print "<body style='background-color:pink'><div align='center'><h3>Your Present Data</h3><table border='5' cellpadding=5px><th>Sensor ID</th><th>Water Availability</th><th>Humidity(%)</th><th>Location</th>"
k=0
for i in f.split('\n'):
	if k==4:
		pass
	else:
		j=i.split()
		print "<tr><td>" + j[0] + "</td><td>" + j[1] + "</td><td>" + j[2] + "</td><td>" + j[3] + "</td></tr>"
	k=k+1
print "</table></div><br/><br/> "
print "<div align='center'><form>"
print "<input type='button' value='Back' onclick='back()'>"
print "<input type='button' value='Maintain' onclick='mantain()'>"
print "<input type='button' value='Save' onclick='save()'>"
print "</form></div></body>"	
