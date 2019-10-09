import numpy as np 
import pandas as pd 
import time 
import csv 
#import import pdb; pdb.set_trace()
filename='AR_1.txt'
series=pd.read_csv(filename)
def OBM(batch_size=0,length):
    T=list()
    for i in range (0,len(series)-batch_size+1):
        t=random.uniform(0, 1)
        hold_list1=series[i:i+batch_size]
        
        hold=int(t*batch_size) 
        if hold==0:
            hold_list2=series[i:i+1]
        else:
            hold_list2=series[i:hold+i]
        print(hold_list2)
        var1=np.var(hold_list1)
        var2=np.var(hold_list2)
      
        
        temp_t=t*size*(np.mean(hold_list1)-np.mean(hold_list2))/(np.var(hold_list1))/(size**(0.5))
        T.append(temp_t)
    mean_T=np.mean(T)
    return mean_T
def BM(Batch_size,Batch_jump,length=len(series)):
	num=int(float(len(series))/float(batch_size))
     	variance=np.var(series[:batch_size*num])
	i=0
    	T=list()
    	while i<len(series) :
        	hold_list=series[i:i+batch_size]
        
        	batch_mean=np.mean(hold_list)
         
        	T.append(batch_mean)
         
        	i=i+batch_jump
    	IAC=batch_size*np.var(T)/variance
    
     
    	return IAC 
        hold=int(t*batch_size) 
       
#series size VS Time 
#series size VS accuracy 
len_vs_t_OBM=[["length","time","value"]]
len_vs_t_BM=[["length","time","value"]]
batch_size=0
for length in range (100,20,len(series)):
    hold_obm=list()
    hold_bm=list()
    #OBM
    start = time.process_time()
    v_obm=OBM(batch_size,length)
    t_obm=time.process_time() - start
    hold_obm.append(length)
    hold_obm.append(t_obm)
    hold_obm.append(v_obm)
    #BM
    start = time.process_time()
    v_bm=BM(batch_size,length)
    t_bm=time.process_time() - start
    hold_bm.append(length)
    hold_bm.append(t_bm)
    hold_bm.append(v_bm)
    len_vs_t_OBM.append(hold_obm)
    len_vs_t_BM.append(hold_bm)
######
myFile = open('OBM_vlength'+'.csv', 'w')
	
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(len_vs_t_OBM)
######
myFile = open('BM_vlength'+'.csv', 'w')
	
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(len_vs_t_BM)


size_vs_t_OBM=[["batch_size","time","value"]]
size_vs_t_BM=[["batch_size","time","value"]]
length=0
for batch_size in range (3,20,len(series)-1):
    hold_obm=list()
    hold_bm=list()
    #OBM
    start = time.process_time()
    v_obm=OBM(batch_size,length)
    t_obm=time.process_time() - start
    hold_obm.append(batch_size)
    hold_obm.append(t_obm)
    hold_obm.append(v_obm)
    #BM
    start = time.process_time()
    v_bm=BM(batch_size,length)
    t_bm=time.process_time() - start
    hold_bm.append(batch_size)
    hold_bm.append(t_bm)
    hold_bm.append(v_bm)
    size_vs_t_OBM.append(hold_obm)
    size_vs_t_BM.append(hold_bm)

######
myFile = open('OBM_vsize'+'.csv', 'w')
	
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(size_vs_t_OBM)
######
myFile = open('BM_vsize'+'.csv', 'w')
	
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(size_vs_t_BM)
