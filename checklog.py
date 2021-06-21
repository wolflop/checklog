# -*- coding:utf-8 -*-
import re
import subprocess
from datetime import datetime
import checkTime

def infoOut(uid):
    a = []
    flag_list = []
    time_list = []
    uid_list = []
    with open('flag.log', 'r') as f:
        for line in f.readlines():
            a.append(line.split())
    for i in range(len(a)):
        uid_list.append(int(re.findall("\\d+", a[i][2])[0]))
        flag_list.append(int(re.findall("\\d+", a[i][1])[0]))
        time_list.append(int(re.findall("\\d+", a[i][0])[0]))
    flag_list_uid = []
    time_list_uid = []
    flag_0_time = []
    counta = 0
    uid_wrong = []
    while counta < len(uid_list):
        if uid_list[counta] == uid:
            flag_list_uid.append(flag_list[counta])
            time_list_uid.append(time_list[counta])
            if flag_list[counta] == 0:
                flag_0_time.append(time_list[counta])
        counta += 1
    if checkFlage(flag_list) and checkTime.checkTime(uid):
        pass
    else:
        uid_wrong.append(uid)
    flag_list_uid.clear()
    time_list_uid.clear()
    return uid_wrong

def checkFlage(flag=[]):
    if (len(flag) % 2) == 0:
        if flag[0] == 1:
            for i in range(len(flag) // 2):
                if flag[2*i] == 1 and flag[2*i-1] == 0:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


if __name__=='__main__':
    #subprocess.call("grep 'scs_n' 1.log|grep 'uid\\[1\\]'| awk '{ print $14,$13,$12}'|sort > 3.log", shell=True)
    subprocess.call(r"grep 'scs_n' ../lcs/mqs-fudao*/log/mqs.log| grep -e 'uid\[[1-2][0-9][0-9]\]' |awk '{print $3,$13,$12}'|sort >flag.log", shell=True)
    subprocess.call(r"grep -e 'uid:[1-2][0-9][0-9] ' ../lcs/mqs-fudao*/log/mqs.log|grep -e 'cmdno:2' |awk '{print $3,$26}'|sort >cmdno.log", shell=True)
    with open (r'/home/service/liuping05/wrongUid.log', 'w+') as f:
        f.write("this is a new test"+'\n')
        for i in range(101, 201):
            if infoOut(i):
                f.write(str(infoOut(i))+'\n')
