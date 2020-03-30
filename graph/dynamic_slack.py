import numpy as np
from collections import Counter
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def p(l,n,x):
    c = 0.0
    tot=0
    for i in range(len(l)):
        tot+=n[i]
        if(l[i]>=x):
            c+=n[i]
    return (c/tot)*100

f1 = open("../slack/data/perl_all","r")
#f2 = open("loadv2_all","r")
#f3 = open("loadv3","r")

slack1 = []
nRef=[]
for line in f1:
    #print(line)
    slack1.append(float(line.split()[3]))
    nRef.append(float(line.split()[4]))



'''
slack3 = []
for line in f3:
    slack3.append(float(line.split()[1]))
'''

x=[y for y in range(0,1000)]
y1 = [p(slack1,nRef, i) for i in x]


#y2 = [p(slack2, i) for i in x]
#y3 = [p(slack3, i) for i in x]

plt.plot(x,y1,label='perl',color='red')
#plt.plot(x,y3,label='v3',color='orange')
plt.legend()
plt.xlabel('Slack in Cycles')
plt.ylabel('Percentage Dynamic Instructions with atleast x Cycles slack')
plt.savefig('perl_all_dynamic.png')