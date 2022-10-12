import csv
import math
with open("data.csv") as f:
    read=csv.reader(f)
    datalist=list(read)
    data=datalist[0]
def mean(data):
    n=len(data)
    total=0
    for d in data: 
        total+=int(d)
    mean=total/n
    return mean
squarelist=[]
for d in data:
    a=int(d)-mean(data)
    a=a**2
    squarelist.append(a)
s_sum=0
for s in squarelist:
    s_sum+=s

result=s_sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(str(standard_deviation))