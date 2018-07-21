#!/usr/bin/python2
import commands
commands.getstatusoutput('yum install tigervnc -y')
commands.getstatusoutput('vncviewer 192.168.43.240:5901')