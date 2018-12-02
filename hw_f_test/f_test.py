import numpy as np
from scipy import stats

data1=[279,338,334,198,303]
data2=[378,275,412,265,286]
data3=[172,335,335,282,250]
data4=[381,346,340,471,318]
data=[data1,data2,data3,data4]

gr_avg=[]
for i in range(4):
    gr_avg.append(np.mean(data[i]))

tot_avg=np.mean(gr_avg)


ssw=0

for i in range(4):
    for j in range(5):
        ssw+=(data[i][j]-gr_avg[i])**2

print("ssw",ssw)
