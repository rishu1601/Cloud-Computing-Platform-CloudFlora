#!/usr/bin/python2
import cgi
import commands
import docker_list
import os
import Cookie
print "Content-Type: text/html"
print
#y=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no 192.168.43.149 systemctl restart docker")
#z=commands.getoutput("sshpass -p redhat ssh -o stricthostkeychecking=no 192.168.43.149 sudo chmod o=rwx /var/run/docker.sock")

print """"
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>CAAS</title>
    <style>
        body {
            background: lightblue !important;
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
        <a id="header-link1" class="header-link" href="../user.html">Home</a>
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
<div id="cass1" align="center">
<h1 style='text-align:center;font-family:verdana;font-color:red;'>CONTAINER AS A SERVICE</h1></br>
<h3 style='text-align:center;font-family:verdana;'>We have these images available</h3>
<pre style='text-align:center;'>"""
docker_list.docker_table()
print"""</table>
</pre>
<form action='/rk/docker-run.py' method='GET'>
What do you want to do? </br>
<input type= 'radio' name='choice' value="pull" height=15px />PULL IMAGE FROM THE DOCKER HUB</br>
<input type= 'radio' name='choice' value="launch" height=15px />LAUNCH CONTAINERS</br>
<input type= 'radio' name='choice' value="install" height=15px />INSTALL BASIC TOOLS AND SERVERS FOR CENTOS:LATEST</br>
<input type='submit' />
</form>
<a href='/rk/docker_manage.py'>Container Management Portal </a>
<br/><br/>
*Please refresh the page if the recently saved image doesn't load
</div>

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
