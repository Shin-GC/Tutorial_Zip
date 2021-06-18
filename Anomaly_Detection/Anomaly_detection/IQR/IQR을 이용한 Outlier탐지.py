import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import seaborn as sns

##########데이터 
path = os.getcwd()
ele = pd.read_csv(
    f"{path}\Temp_data.csv", parse_dates=True,names=['time','values'],header=1)
print(ele['values'])

v_min = ele['values'].min()
v_max = ele['values'].max()
v_median = ele['values'].median()
print(f'min값: {v_min}')
print(f"max값: {v_max}")
print(f"median값: {v_median}")

'''
# 그래프 표시 ( x는 값 y는 중복 수,kde는 선 표시 여부, bins는 그래프 표, rug는 커널밀도 )
#hist 옵션: 히스토그램, rug 옵션: 데이터의 위치를 나타내는 선분 표시
sns.displot(ele['values'],bins=30,kde=True,rug=True, rug_kws={"color": "r", "alpha":0.3, "linewidth": 2, "height":0.2 })

'''

                                                                                                                
def outlier_iqr(data,column):
    global lower,upper
    q25,q75= np.quantile(data[column],0.25),np.quantile(data[column],0.75)
    #iqr계산
    iqr = q75-q25
    #outlier cutoff 계산
    cut_off = iqr *1.5
    #lower와 upper bound 값 구하기
    lower, upper = q25 - cut_off, q75 + cut_off
    print(f'IQR 값 : {iqr}')
    print(f'lower bound값: {lower }')
    print(f'upper bound값: {upper}')
    data1 = data[data[column]>upper]
    data2 = data[data[column]<lower]
    return print(f"총 이상치 갯수: {data1.shape[0] + data2.shape[0]} 이다.")

outlier_iqr(ele,'values')

sns.displot(ele['values'],kde=False)
plt.axvspan(xmin=lower, xmax=v_min,alpha=0.2,color='red')
plt.axvspan(xmin=upper, xmax=v_max,alpha=0.2,color='red')
plt.show()

"""
print(ele['values'].min()) #2
print(ele['values'].max()) #91
print(ele['values'].median()) #6.0

quartile_0 = ele['values'].quantile(0) #percentile (같은 데이터 수로 100 등분), decile (같은 데이터 수로 10 등분), quartile (같은 데이터 수로 4 등분) #최소값
quartile_1 = ele['values'].quantile(0.25) #1 사분위수 (25% 지점수)
quartile_2 = ele['values'].quantile(0.5) #2 사분위수 (50% 지점수, 중앙값 (median))
quartile_3 = ele['values'].quantile(0.75) #3 사분위수 (70% 지점수)
quartile_4 = ele['values'].quantile(1) #최대값
print(quartile_0) #2.0
print(quartile_1) #3.0
print(quartile_2) #6.0
print(quartile_3) #8.5
print(quartile_4) #91.0
IQR = quartile_3 - quartile_1
print(IQR) #5.5
print(1.5 * IQR) #8.25
print(quartile_1 - 1.5 * IQR) #-5.25
print(quartile_3 + 1.5 * IQR) #16.75
search_df = ele[(ele['values'] < (quartile_1 - 1.5 * IQR)) | (ele['values'] > (quartile_3 + 1.5 * IQR))]
print(search_df)
"""
