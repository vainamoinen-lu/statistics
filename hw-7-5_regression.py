import numpy as np

samplex=[0.34,1.38,-0.65,0.68,1.4,-0.88,-0.30,-1.18,0.50,-1.75]
sampley=[.27,1.34,-.53,.35,1.28,-.98,-.72,-.81,.64,-1.59]
mean_x=np.mean(samplex)
mean_y=np.mean(sampley)

s_xx=0
n=10
for i in range(n):
    s_xx+=(samplex[i]-mean_x)**2

s_xy=0
for i in range(n):
    s_xy+=(samplex[i]-mean_x)*(sampley[i]-mean_y)

s_yy=0
for i in range(n):
    s_yy+=(sampley[i]-mean_y)**2

b_estimate=s_xy/s_xx
a_estimate=mean_y-b_estimate*mean_x

d_estimate=s_xy/s_yy
c_estimate=mean_x-d_estimate*mean_y

print("b=",b_estimate)
print("a=",a_estimate)
print("d=",d_estimate)
print("c=",c_estimate)