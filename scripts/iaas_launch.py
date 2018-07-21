#!/usr/bin/python2


import cgi
import commands

print "content-type:  text/html"
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
            background: green !important;
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

    <div id="main-container">"""
caas_server_password="redhat"
caas_server_ip="192.168.43.240"
OS_Name=cgi.FormContent()['OS_Name'][0]
cpu_count=cgi.FormContent()['cpu_count'][0]
Hard_Disk_Size=cgi.FormContent()['Hard_Disk_Size'][0]
ram_size=cgi.FormContent()['ram_size'][0]
client_ip=cgi.FormContent()['client_IP'][0]
client_password=cgi.FormContent()['client_password'][0]
port_number=cgi.FormContent()['port_number'][0]
launch_os="sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo virt-install --name {2} --location /os/rhel-server-7.3-x86_64-dvd.iso  --os-type linux --os-variant rhel7 --memory {5} --vcpus {3} --disk  /var/lib/libvirt/images/{2}.qcow2,size={4} --graphics  vnc,password={6},listen=0.0.0.0,port={7}  --noautoconsole".format(caas_server_password,caas_server_ip,OS_Name,cpu_count,Hard_Disk_Size,ram_size,client_password,port_number)

os_launch_status=commands.getstatusoutput(launch_os)

if os_launch_status[0] == 0:
	f=open('/content/scripts/launch_os.py','w+')
	run_os="#!/usr/bin/python2\nimport commands\ncommands.getstatusoutput('yum install tigervnc -y')\ncommands.getstatusoutput('vncviewer {0}:{1}')".format(caas_server_ip,port_number)
	f.write(run_os)
	f.close()
	commands.getoutput("chmod +x launch_os.py")
	install_tigervnc_status=commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /content/scripts/launch_os.py root@{1}:/root/Desktop/".format(client_password,client_ip))
	print "<div align='center'><p><i>Your OS has been launched successfuly on the given IP</i><br/>Please use the password you provided to access the system<br/>Please double click the executable file on Client's Desktop</p><a href='iaas_manage.py'>OS MANAGEMENT PORTAL</a><div>"
else:
	print "<div align='center'><h1>The Port might be busy or there may be some other errors<h1><br/><b>Sorry for Inconveniences....Please try Again<b><br/><a href='../iaas.html'>Click Here Please</a></div>"



print """</div>

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
