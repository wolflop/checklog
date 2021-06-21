# -*- coding:utf-8 -*-
import re

def cmdnoTime(uid):
    cmdnoTimeList = []
    with open("cmdno.log", 'r') as f:
        for line in f.readlines():
            #print(line.split())
            a = (re.findall("\\d+", line.split()[1]))[0]
            if int(a) == 100:
                #print(line.split()[0])
                cmdnoTimeList.append(line.split()[0])
    return cmdnoTimeList

if __name__=='__main__':
    print(cmdnoTime(100))
