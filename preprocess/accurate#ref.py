import numpy as np
from collections import Counter
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def p(l,x):
    c = 0.0
    for i in range(len(l)):
        if(l[i]<=x):
            c+=1
    return (c/len(l))*100

f1 = open("../slack/data/mcf_load","r")


sum_all=0
sum1=0
l=0
l_all=0
for line in f1:
    #print(line)
    if(int(line.split()[3])>3295):
        sum1+=int(line.split()[3])
        l+=1
    sum_all+=int(line.split()[3])
    l_all+=1
    
    
    #sum_all+=int(line.split()[3])
print(float(sum1)/float(sum_all),float(l)/float(l_all))
