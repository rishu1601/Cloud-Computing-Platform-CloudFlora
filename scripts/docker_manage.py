#!/usr/bin/python2
import cgi
import commands
print "Content-Type: text/html"
print

print """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>HOME PAGE</title>
    <style>
        body {
            background: lightgrey !important;
        }
	table#tab tr:nth-child(odd)
	{
	  background-color: white; 
	}
	table#tab tr:nth-child(even)
	{
	  background-color: #eee; 
		text-align:left;
	}
	table#tab th
	{
		background-color:black;
		color:white;
	}
        #header {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            background: #333333;
        }

        #logo {
            position: relative;
            width: 85px;
            float: left;
        }
	#save
	{
		background-color:PowderBlue;
		color:black;
	}
	#shell
	{
		background-color:brown;
		color:black;
	}
	#start
	{
		background-color:green;
		color:black;
	}
	#stop
	{
		background-color:yellow;
		color:black;
	}
	#remove
	{
		background-color:red;
		color:black;
	}
        .header-link {
            padding: 3px 6px;
            font-weight: 600;
            color: #e9e9e9;
            margin: 0 0 0 50px;
            position: relative;
            top: 22px;
            text-decoration: none;
            font-size: 25px;
        }

        #header-link4 {
            font-size: 25px;
            padding: 3px 10px;
        }

        #header-link5 {
            right: 10px;
            float: right;
        }

        #main-container {
            margin: 100px 0 0 0;
            position: relative;
            float: inherit;
            min-height: 1000px;
            width: 100%;
            height: auto;
        }

        #page-footer {
            position: relative;
            /* bottom: 0; */
            /* left: 0; */
            /* right: 0; */
            width: 100%;
            height: 50px;
            background: #333;
            padding: 10px;
            float: left;
            margin: 10px 0 0 -12px;
        }

        .footer_btn {
            padding: 3px 5px;
            text-decoration: none;
            font-size: 20px;
            font-weight: 600;
            color: #e9e9e9;
            margin: 0 0 0 20px;
            }

        .homepage-img {
            width: 100%;
        }
    </style>
    <script type="text/javascript">
    </script>
</head>

<body>

    <div id="header">
        <!-- Page Header -->
        <img id="logo" src="../images/logo.jpg" alt="company logo">
        <a id="header-link1" class="header-link" href="index.html">Home</a>
        <select id="header-link4" class="header-link" style="background: #333333; border: 0px;">
    <option value="dropdown1"><a href="#">Services</a></option><br/>
<option value="dropdown2"><a href="iot.html">Iot</a></option><br/>
<option value="dropdown3"><a href="cloudflora.html">Cloud Flora</a></option><br/>
<option value="dropdown4"><a href="/rk/caas.py">Caas</a></option>
<option value="dropdown4"><a href="staasmain.py">STaas</a></option>
<option value="dropdown4"><a href="iaas.html">Iaas</a></option>
        </select>
            </div>

    <div id="main-container">
	<script>
function dock_start(cont_name)
{
	document.location='docker_start.py?x=' + cont_name;
}
function dock_stop(cont_name)
{

	document.location='docker_stop.py?x=' + cont_name;
}

function dock_remove(cont_name)
{

	document.location='docker_remove.py?x=' + cont_name;
}
function dock_shell(cont_name)
{

	document.location='docker_shell.py?x=' + cont_name;
}
function dock_save(cont_name)
{

	document.location='docker_save.py?x=' + cont_name;
}
</script>"""
z=1
print "<div align='center'><h3>CONTAINER MANAGEMENT PORTAL</h3></hr><table id='tab' border='5' cellpadding=5px><th>Image Name</th><th>Container Name</th><th>IP Address</th><th>Status</th><th>Start</th><th>Stop</th><th>Remove</th><th>Online Shell</th><th>Save Image</th>"
for i in commands.getoutput('sudo docker ps -a').split('\n'):
	if z==1:
		z=z+1
		pass
	else:
		j=i.split()
		con_status=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
		ip_address=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.IPAddress'".format(j[-1]))
		print "<tr><td>" + j[1] + "</td><td>" + j[-1] + "</td><td>" + ip_address + "</td><td>" + con_status + "</td><td><input value='" + j[-1] + "'type='button' name='start' id='start' onclick=dock_start(this.value) /> " + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_stop(this.value) id='stop'/>" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_remove(this.value) id='remove' />" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_shell(this.value) id='shell' />" + "</td><td><input value='" + j[-1] + "'type='button' onclick=dock_save(this.value) id='save'/>" + "</td></tr>"
print"</table></div></hr><div align='center'><a href='caas.py'>Go Back</a></div>"



print"""</div>

    <div id="page-footer" class="">
        <a id="footer_btn1" class="footer_btn" href="#">About us</a>
        <a id="footer_btn2" class="footer_btn" href="#">Linux World Jaipur</a>
        <a id="footer_btn3" class="footer_btn" href="#">Future Projects</a>
        <a id="footer_btn4" class="footer_btn" href="#">Contact us </a>
        <a id="footer_btn4" class="footer_btn" href="#">Team </a>
    </div>

</body>

</html>

"""
