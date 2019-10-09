import numpy as np
import pandas as pd
import csv
from datetime import datetime
#import pdb; pdb.set_trace()
filename='/work/06206/deng451e/stampede2/APS/MC.txt'
data=pd.read_csv(filename )
series=list(data['avgLogLiso'])



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


size_vs_t_BM=[["batch_size","time","IAC"]]
hold=int(len(series)**0.66666)

print(len(series))
for batch_size in range (hold-100,hold+100):
	print("good")
    	hold_bm=list()
    	#BM
	batch_jump=batch_size
	start = datetime.now()
        v_bm=BM(batch_size,batch_jump)
        end = datetime.now()
        time_d = end - start
        time_d_float = time_d.total_seconds()
    	hold_bm.append(batch_size)
    	hold_bm.append(time_d_float)
    	hold_bm.append(v_bm)
	size_vs_t_BM.append(hold_bm)

######
myFile = open('BM_batch_size_MC'+'.csv', 'w')
with myFile:
        writer = csv.writer(myFile)
        writer.writerows(size_vs_t_BM)

