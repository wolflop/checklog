#-*- coding:utf-8 -*-
from datetime import datetime
import re
def checkTime(uid):
    cmdnoTime = []
    with open ('cmdno.log', 'r') as f:
        for line in f.readlines():
            if int((re.findall(r"\d+", line.split()[1]))[0]) == uid:
                cmdnoTime.append(datetime.strptime(line.split()[0][0:8], "%H:%M:%S"))
    flageTime = []
    with open ('flag.log', 'r') as f:
        for line in f.readlines():
            #print(line.split()[0],line.split()[1],line.split()[2])
            if int((re.findall(r"\d+", line.split()[2]))[0]) == uid and int(re.findall(r"\d+", line.split()[1])[0]) == 0:
                flageTime.append(datetime.strptime(line.split()[0][0:8], "%H:%M:%S"))
    if len(cmdnoTime) != len(flageTime):
        return False
    else:
        for i in range(len(cmdnoTime)):
            if str(flageTime[i] - cmdnoTime[i]) != ("0:00:05"):
                return False
            else:
                return True
