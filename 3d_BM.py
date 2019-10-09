import numpy as np 
import pandas as pd
import csv 
from datetime import datetime
# import pdb; pdb.set_trace()
filename='/work/06206/deng451e/stampede2/APS/MC.txt'
data=pd.read_csv(filename) 
series=data['avgLogLiso']
 
     
def BM(Batch_size,Batch_jump,length=len(series)):
	num=int(float(len(series))/float(batch_size))
	i=0
    	T=list()
    	while i<len(series) :
        	hold_list=series[i:i+batch_size]
        	batch_mean=np.mean(hold_list)
        	T.append(batch_mean)
        	i=i+batch_jump
    	variance=np.var(series[:i]) #effective series variance
    	IAC=batch_size*np.var(T)/variance
    	return IAC

ddd=[["batch_size","batch_jump","IAC"]]
hold=int(len(series)**0.666666)
for batch_size in range (hold-100,hold+100):
	for batch_jump in range (hold-100,hold+100):     
        	print(batch_jump)
        	hold_bm=list()
        
       		 #BM
       		v_bm=BM(batch_size,batch_jump)
   
        	hold_bm.append(batch_size)
	        hold_bm.append(batch_jump)
	        hold_bm.append(v_bm)
	        ddd.append(hold_bm)
######
myFile = open('3d_graph'+'.csv', 'w')
with myFile:
	writer = csv.writer(myFile)
	writer.writerows(ddd)
 

