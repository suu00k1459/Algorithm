from datetime import datetime
import time
import math

def solution(fees, records):
    

    def trs_m(dt):
        d = datetime.strptime(dt, "%H:%M")
        return d.hour*60 + d.minute


    rec = {}
    rst = []

    for i in records:
        if i.split()[1] not in rec:
            rec[i.split()[1]]=[(trs_m(i.split()[0]))]
        else :
            rec[i.split()[1]].append(trs_m(i.split()[0]))

    for i in rec.keys():
        if len(rec[i])%2 ==0:
            rec[i]=sum([bi-ai for ai, bi in zip(rec[i][::2],rec[i][1::2])])
        else :
            rec[i].append(trs_m('23:59'))
            rec[i]=sum([bi-ai for ai, bi in zip(rec[i][::2],rec[i][1::2])])



    for i in sorted(rec.keys()):
        if rec[i]<= fees[0]:
            rst.append(fees[1])
        
        else :
            rst.append(fees[1] + math.ceil((rec[i]-fees[0])/fees[2])*fees[3])

    return rst