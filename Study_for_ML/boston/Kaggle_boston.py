import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import os
from keras.callbacks import ModelCheckpoint

train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")
len_train = len(train)
print(f"Train Shape : {train.shape}\nTest Shape : {test.shape}")

#print("Skewness: %f" % data['SalePrice'].skew()) #왜도가 1.8로 0보다 크므로 왼쪽으로 치우친 모양
#print("Kurtosis: %f" % data['SalePrice'].kurt()) #척도가 6으로 큰 양수 이므로 매우 뾰족한 모양을 가진다.
#sns.displot(data['SalePrice'], kde = True ) # 왜도가 높아 왼쪽으로 치우치고 척도가 높아 뾰족한 모습으로 나타나는 그래프.
train_corr = train.corr()
top_corr = train[train_corr.nlargest(10,'SalePrice')['SalePrice'].index]
#print(top_corr.columns)
#fig = plt.subplots(figsize=(13,8))
#fig = sns.heatmap(top_corr.corr(), annot = True)
#plt.show()

Y_train = train['SalePrice']
#train 값 중 필요한 결과값인 SalePrice값을 따로 저장
print(f"합치기 전 Train : {train.shape}")
train = train[list(test)]
train = pd.concat([train, test], axis=0, ignore_index=True)
#test의 값들과 합치기 위해 test와 같은 column명을 가진 애들만 저장
print(f"합친 후 Train : {train.shape}")

#data = pd.concat([train['OverallQual'], Y_train], axis = 1)
# axis 가 1 이면 기존 인덱스를 그대로 이어서 사용한다. 1,3 인덱스와 2,3,4 가 합쳐지면 1,2,3,4 가 된다.
#fig = plt.subplots( figsize= (13,8) )
#fig = sns.boxplot(x= "OverallQual", y="SalePrice", data= data)
#plt.show()

# NULL값 처리
total = train.isnull().sum().sort_values(ascending=False) # 내림차 순 [Defualt= 오름차순]
# null 의 갯수
percent = (train.isnull().sum() / train.isnull().count()).sort_values(ascending=False)
#sum 함수는 null 값만 찾고, count는 null 값을 포함한다.
# 전체 데이터에 몇%의 null이 존재하는지
#print(total.head(5))
#print(percent.head(5))

missing_data = pd.concat([total, percent], axis=1, keys=("Total", "Percent"))
#print(missing_data[ missing_data["Total"] > 1 ].tail(5))
#print(missing_data[ missing_data["Total"] > 1 ].index)

train = train.drop((missing_data[ missing_data["Total"] > 1 ]).index, axis=1 )
#하나를 삭제 하고 싶을땐 아래와 같이 코드를 구성한다.
train = train.drop( train.loc[ train['Electrical'].isnull() ].index)
#이때 loc는 위치를 반환해주는 함수이다.
print(f"Drop 후 Train 상태 :{train.shape}")

# 이상치 제거

#out = "GrLivArea"
#data = pd.concat( [ Y_train, train[out] ], axis = 1 )
#data.plot.scatter( x = out, y = 'SalePrice', ylim = (0,800000))
#plt.show()

#print(train.sort_values(by = 'GrLivArea', ascending = False)[:2])
# 표에서 오른쪽 하단으로 갈 수록 큰 값이었으므로 내림차 순으로 앞에 2개 값에 해당한다.
train = train.drop ( train[ train['Id'] == 1299 ].index)
train = train.drop ( train[ train['Id'] == 524 ].index)
#print(train.sort_values(by = 'GrLivArea', ascending = False)[:2])
#sns.distplot(Y_train, kde = True)
#fig = plt.figure()
#fig = stats.probplot(Y_train, plot=plt)
# stats.probplot로 주어진 데이터의 정규분포와의 QQ plot 를 그릴 수 있다. 이때 dist 옵션을 이용해 다른 분포와 비교도 가능하다.
#plt.show()
Y_train = np.log1p(Y_train) #x값이 0일때 y값이 무한대가 되지 않게 하기 위해 np.log 대신 np.log1p를 사용
#sns.distplot(Y_train, kde = True)
#fig = plt.figure()
#fig = stats.probplot(Y_train, plot=plt)
# stats.probplot로 주어진 데이터의 정규분포와의 QQ plot 를 그릴 수 있다. 이때 dist 옵션을 이용해 다른 분포와 비교도 가능하다.
#plt.show()
#print("Skewness: %f" % Y_train.skew()) #왜도가 0.12로 0과 가깝기 때문에 한쪽에 편향되지 않고 가운데에 위치한다.
#print("Kurtosis: %f" % Y_train.kurt()) #척도가 0.80으로 1과 가깝기 때문에 완만하다.

#sns.set()
#cols = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
#sns.pairplot(train[cols], size = 1.5)
#plt.show()

#print("Skewness: %f" % train['GrLivArea'].skew()) #왜도가 1.01로 0보다 크기 때문에 왼쪽으로 편향되어 있다.
#print("Kurtosis: %f" % train['GrLivArea'].kurt()) #척도가 2.05로 0보다 크기때문에 정규분포 보다 뾰족한 형태를 취한다.

#sns.displot( train['GrLivArea'], kde = True )
#fig = plt.figure()
#stats.probplot( train['GrLivArea'], plot = plt )
#plt.show()

train['GrLivArea'] = np.log1p( train['GrLivArea'] )

#print("Skewness: %f" % train['GrLivArea'].skew()) #왜도가 -0.07로 0에 매우 가까우므로 한쪽으로 편향되지 않고 가운데에 고르게 분포되어있다.
#print("Kurtosis: %f" % train['GrLivArea'].kurt()) #척도가 0.09로 0에 매우 가까우므로 완만한 형태의 그래프를 그려준다.


#sns.displot( train['GrLivArea'], kde = True )
#fig = plt.figure()
#stats.probplot( train['GrLivArea'], plot = plt )
#plt.show()

#print("Skewness: %f" % train['TotalBsmtSF'].skew()) #왜도가 
#print("Kurtosis: %f" % train['TotalBsmtSF'].kurt()) #척도가 

#sns.displot( train['TotalBsmtSF'] ,kde = True)
#fig = plt.figure()
#stats.probplot( train['TotalBsmtSF'], plot = plt )
#plt.show()

#만약 0이 아닌 값이라면 1을 대입, 0이라면 0을 대입시킨다.
train['HasBsmt'] = pd.Series(len(train['TotalBsmtSF']), index=train.index)
train['HasBsmt'] = 0 
train.loc[train['TotalBsmtSF']>0,'HasBsmt'] = 1
# 새로운 column에 TotalBsmtSF의 값이 0이 아니라면 1을 넣고 아닌 나머지는 0을 넣는 식으로 값을 생성
train.loc[train['HasBsmt']==1,'TotalBsmtSF'] = np.log1p(train['TotalBsmtSF'])

#sns.distplot(train[train['TotalBsmtSF']>0]['TotalBsmtSF'], fit=norm)
#fig = plt.figure()
#res = stats.probplot(train[train['TotalBsmtSF']>0]['TotalBsmtSF'], plot=plt)
#plt.show()
print(train.shape)
train = pd.get_dummies(train)

print(train.shape)

X_train = train[:len_train]
Y_train = train[len_train:]
print(X_train.shape, Y_train.shape)

early_stopping_callback = EarlyStopping(monitor='loss', patience=100,verbose=1)

model = Sequential()
model.add(Dense(64, input_dim = X_train.shape[1], activation = 'relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

model.compile( loss='mean_squared_error',
              optimizer='adam', metrics=['accuracy'])

model.fit(X_train,Y_train , epochs=1000, batch_size=100, callbacks=[early_stopping_callback])
