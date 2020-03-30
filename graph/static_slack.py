import numpy as np
from collections import Counter
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def p(l,x):
    c = 0.0
    for i in range(len(l)):
        if(l[i]>=x):
            c+=1
    return (c/len(l))*100

f1 = open("../slack/data/perl_load","r")
#f2 = open("loadv2_all","r")
#f3 = open("loadv3","r")

slack1 = []
for line in f1:
    #print(line)
    slack1.append(float(line.split()[3]))
'''
slack2 = []

for line in f2:
    #print(line)
    slack2.append(float(line.split()[2]))
'''

'''
slack3 = []
for line in f3:
    slack3.append(float(line.split()[1]))
'''

x=[y for y in range(0,200)]
y1 = [p(slack1, i) for i in x]
#y2 = [p(slack2, i) for i in x]
#y3 = [p(slack3, i) for i in x]

plt.plot(x,y1,label='v1',color='red')
#plt.plot(x,y2,label='v2',color='green')
#plt.plot(x,y3,label='v3',color='orange')
plt.legend()
plt.xlabel('Slack in Cycles')
plt.ylabel('Percentage Static loads with atleast x Cycles slack')
plt.savefig('perl_load_static.png')