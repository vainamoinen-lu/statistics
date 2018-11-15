import numpy as np

data0=[1.7,1.9,6.1,12.5,16.5,25.1,30.5,42.1,82.5]
data1=[13.6,19.8,25.2,46.2,46.2,61.1]
data2=[13.4,20.9,25.1,29.7,46.9]
data=[data0,data1,data2]

def w_average(val_list,w_list):
    res=0
    list_len=len(val_list)
    for i in range(list_len):
        res+=val_list[i]*w_list[i]
    res=res/np.sum(w_list)
    return res

gr_avg=[]
for i in range(3):
    gr_avg.append(np.mean(data[i]))
tot_avg=w_average(gr_avg,[len(data0),len(data1),len(data2)])

num_list=[9,6,5]

# ssb=0
# for i in range(3):
#     ssb+=num_list[i]*((gr_avg[i]-tot_avg)**2)
# print("ssb=",ssb)
ssw=0
for i in range(3):
    for j in range(num_list[i]):
        ssw+=(data[i][j]-gr_avg[i])**2
print("ssw=",ssw)      