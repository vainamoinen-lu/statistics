import numpy as np

def regression():
    sample_y=[0.08088,0.04737,-0.04634,0.16834,-0.09082]
    sample_xm=[-0.01309,0.15958,0.09966,0.03125,0.06206]
    sample_xs=[-0.08463,0.02884,0.00165,0.09571,-0.05723]
    sample_xh=[-0.13373,0.03616,0.07919,0.09227,-0.13242]

    B=np.array([np.ones(5),sample_xm,sample_xs,sample_xh])
    B=B.T

    inv=np.linalg.inv(np.matmul(B.T,B))
    sample_y=np.array(sample_y)
    BETA=np.matmul(inv,B.T)
    BETA=np.matmul(BETA,sample_y.T)

    # print("BETA:")
    # print(BETA)

    EPSILON=sample_y-np.matmul(B,BETA)
    rss=(np.linalg.norm(EPSILON))**2
    # print("rss:")
    # print(rss)

    y_avg=np.mean(sample_y)
    tss=0
    for i in range(5):
        tss+=(sample_y[i]-y_avg)**2
    # print("tss:")
    # print(tss)
    return BETA


BETA=regression()
y=[0.1,0.06629,-0.11545,0.02008,-0.08268]
xm=[0.02604,0.07851,0.06732,-0.06483,-0.09029]
xs=[0.02695,0.02362,0.23938,0.06127,-0.05773]
xh=[0.00211,-0.04,0.35526,0.10714,-0.02933]
B=np.array([np.ones(5),xm,xs,xh])
B=B.T
y=np.array(y)
EPSILON=y-np.matmul(B,BETA)
res4=np.linalg.norm(EPSILON)
print("res4:",res4)
y_avg=np.mean(y)
tss=0
for i in range(5):
    tss+=(y[i]-y_avg)**2
print("tss:")
print(tss)
