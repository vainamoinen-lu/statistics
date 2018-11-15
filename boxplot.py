

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



data1=[279,338,334,198,303]
data2=[378,275,412,265,286]
data3=[172,335,335,282,250]
data4=[381,346,340,471,318]
boxplot_data=pd.DataFrame({'group1':data1,'group2':data2,'group3':data3,'group4':data4})
boxplot_data.boxplot()
plt.xlabel('group index')
plt.ylabel('result')
plt.savefig('boxplot.png')