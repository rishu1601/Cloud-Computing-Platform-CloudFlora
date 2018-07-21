#!/usr/bin/python2
import cgi,cgitb
import commands
import docker_list
print "content-type: text/html"
print

print"""
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>HOME PAGE</title>
    <style>
        body {
            background: orange !important;
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


"""
choice=cgi.FormContent()['choice'][0]
if choice=='pull':
     print"<form action='/rk/docker-pull.py'>Enter the image name you want : <input name='ds'/><input type='submit' value='get'/></form><input type='submit' value='Back' formaction='caas.py'>"
elif choice=='launch':
	print "<form action='docker_launch.py'>No. of Containers required : <input type='number' id='f2' name='container_count'/><input type='submit' value='Launch'/><input type='submit' value='Back' formaction='caas.py'></form>"
elif choice=='install':
	print """
<form action='/rk/docker-initialize.py' id='f3'>
<h3>Choose the services</h3>\t\t\t\t\t
<input type='checkbox' name='httpd'/>HTTPD<br/>\t\t\t\t
<input type='checkbox' name='net-tools'/>NET-TOOLS<br/>\t\t\t\t
<input type='checkbox' name='nfs'/>NFS<br/>\t\t\t\t
<input type='checkbox' name='ssh-server'/>OPEN-SSH-SERVER<br/>
<input type='checkbox' name='ssh-client'/>OPEN-SSH-CLIENT<br/>
<input type='checkbox' name='python2'/>PYTHON2
<center><h4>Enter the image Name : <input type='text' name='image_name'>
Version : <input type='text' name='version'></h4>
<input type='submit' value='Install and Save Changes'></center>
<center><input type='submit' value='Back' formaction='caas.py'></center>
</form>

    </div>

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
