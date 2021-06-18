import os
import pandas as pd
import numpy as np
import transform
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import SeasonalAD
from matplotlib import pyplot as plt
path = os.getcwd()
transform.savecsv()
s_train = pd.read_csv("./temp_data.csv", index_col="timestamp", parse_dates=True, squeeze=True)
s_train = validate_series(s_train)
"""
from adtk.detector import InterQuartileRangeAD #IQR을 이용한 데이터 이상치 검사
iqr_ad = InterQuartileRangeAD(c=1.5) 
anomalies = iqr_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()
""" 
#이상 값이 아닌 정상 데이터여도 값이 평균보다 살짝만 낮아도 이상으로 탐지하는 문제가 있으므로 사용 X
"""
from adtk.detector import QuantileAD
quantile_ad = QuantileAD(high=0.99, low=0.01)
anomalies = quantile_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()
"""
#IQR방식과 마찬가지로 백분율로 나눠 이상치가 아니여도 백분율 100퍼 혹은 0.01퍼의 값을 탐지해내 문제가 없는 데이터여도 탐지하므로 사용 X
from adtk.detector import GeneralizedESDTestAD
esd_ad = GeneralizedESDTestAD(alpha=0.3)
# alpha는 학습 데이터 적합 정도와 회귀 계수 값을 크기 제어를 수행하는 튜닝 파라미터
anomalies = esd_ad.fit_detect(s_train) # anomaly 값을 fit_detct를 통해 탐지
plot(s_train, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
plt.show()
#
#ts_linewidth = 선 굵기 , ts_markersize = 원 크기 , anomaly_markersize = anomaly의 점 크기 , anomaly_color = 이상치 표현 원 색깔 \
