import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import os
from keras.callbacks import ModelCheckpoint

df_train = pd.read_csv('./train.csv')
print(df_train.head())

print(df_train.columns) #columns 조회

print(df_train['SalePrice'].describe())

#sns.histplot(df_train['SalePrice'])
#plt.show()

print("Skewness: %f" % df_train['SalePrice'].skew()) #왜도가 1.8로 1보다 크므로 왼쪽으로 치우친 모양
print("Kurtosis: %f" % df_train['SalePrice'].kurt()) #척도가 6으로 큰 양수 이므로 매우 뾰족한 모양을 가진다.

#var = df_train['GrLivArea']
#data = pd.concat([df_train['SalePrice'],var], axis = 1)

#data.plot.scatter( x = 'GrLivArea', y = 'SalePrice',  ylim=(0,800000))
#plt.show()

#var = df_train['OverallQual']
#data = pd.concat([df_train['SalePrice'],var], axis = 1)

#fig = plt.subplots(figsize=(8,6))

#fig = sns.boxplot (x = 'OverallQual', y = 'SalePrice', data= data)
#fig.axis(ymin=0, ymax=800000)
#plt.show()

#var = 'YearBuilt'
#data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
#f, ax = plt.subplots(figsize=(16, 8))
#fig = sns.boxplot(x=var, y="SalePrice", data=data)
#fig.axis(ymin=0, ymax=800000)
#plt.xticks(rotation=90)
#plt.show()

df_corr = df_train.corr()
top_corr = df_corr.index[abs(df_corr['SalePrice'])>=0.5]
print(top_corr)

#fig= plt.subplots(figsize=(13,8))
#fig = sns.heatmap(df_train[top_corr].corr(), annot = True, cmap = "RdYlGn")
#fig = sns.heatmap(df_train[top_corr.index], annot = True, cmap = 'RdYlGn')

#data = pd.concat([df_train['YearRemodAdd'],df_train['SalePrice']],axis=1)
#ax = plt.subplots(figsize=(13,8))
#ax = sns.boxplot( x = "YearRemodAdd", y= "SalePrice",  data = data)

#data = pd.concat([df_train['GarageCars'],df_train['SalePrice']],axis=1)
#fig = plt.subplots(figsize=(13,8))
#fig = sns.boxplot( x= "GarageCars", y = "SalePrice", data = data)

#corrmat = df_train.corr()
#f, ax = plt.subplots(figsize=(12, 8))
#sns.heatmap(corrmat, vmax=.8, square=True, annot = True, annot_kws= {"size":5})
#plt.show()

#cols = df_corr.nlargest(10, 'SalePrice')['SalePrice'].index
#nlargest 가장 큰 수를 찾아내는 함수로 SalePrice와 관련된 것 중 상관관계가 가장 높은 10개를 저장
#cm = np.corrcoef(df_train[cols].values.T)
#sns.set( font_scale = 1.25)
#hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
#plt.show() 
sns.set() #초기화
#cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
#sns.pairplot(df_train[cols], size = 2.5)
#plt.show()
total = df_train.isnull().sum().sort_values(ascending=False) #내림차순
percent = (df_train.isnull().sum() / df_train.isnull().count()).sort_values(ascending = False)
missing_data = pd.concat([total, percent], axis=1, keys = ['Total', 'Percent']) #keys 값을 줘 계층적 인덱스 주기
#sum 함수는 null 값만 찾고, count는 null 값을 포함한다.
#print(missing_data.head(20))
df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1)
df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)

print(f"존재하는 Missing_Data: {df_train.isnull().sum().max()}") #남은 missing_data 체크

saleprice_scaled = StandardScaler().fit_transform(df_train['SalePrice'][:,np.newaxis]) #정규화 및 차원 변경 [ 배열 차원 ]

low_range = saleprice_scaled[saleprice_scaled[:,0].argsort()][:10]
high_range= saleprice_scaled[saleprice_scaled[:,0].argsort()][-10:]
#print(f"원래 모양:{df_train.shape}\n변화 후 모양:{saleprice_scaled.shape}")
#print('outer range (low) of the distribution:')
#print(low_range)
#print('\nouter range (high) of the distribution:')
#print(high_range)

del_vel =df_train.sort_values(by = 'GrLivArea', ascending = False)[:2]['Id']

df_train = df_train.drop(df_train[df_train['Id'] == 1299].index)
df_train = df_train.drop(df_train[df_train['Id'] == 524].index)


#sns.displot(df_train['SalePrice'], kde=True)
#fig = plt.figure()
#res = stats.probplot(df_train['SalePrice'], plot=plt)

df_train['SalePrice'] = np.log(df_train['SalePrice'])
#sns.displot(df_train['SalePrice'], kde=True)
#fig = plt.figure()
#res = stats.probplot(df_train['SalePrice'], plot=plt)
#plt.show()

df_train['GrLivArea'] = np.log(df_train['GrLivArea'])

#sns.displot(df_train['GrLivArea'], kde = True)
#fig = plt.figure()
#res = stats.probplot(df_train['GrLivArea'], plot=plt)
#plt.show()

df_train['HasBsmt'] = pd.Series(len(df_train['TotalBsmtSF']), index=df_train.index)
df_train['HasBsmt'] = 0 
df_train.loc[df_train['TotalBsmtSF']>0,'HasBsmt'] = 1

df_train.loc[df_train['HasBsmt']==1,'TotalBsmtSF'] = np.log(df_train['TotalBsmtSF'])

df_train = pd.get_dummies(df_train)

print(df_train.shape)
print(df_train.head(10))
dataset = df_train.values

X = dataset[:,1:221]
Y = dataset[:,221]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

early_stopping_callback = EarlyStopping(monitor='loss', patience=1000,verbose=1)
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
   os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath="./model/{epoch:02d}-{accuracy:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='accuracy', verbose=1, save_best_only=True)


model = Sequential()
model.add(Dense(30, input_dim = X_train.shape[1], activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

model.compile( loss='mean_squared_error',
              optimizer='adam', metrics=['accuracy'])

model.fit(X_train,Y_train , epochs=10000, batch_size=100, callbacks=[early_stopping_callback, checkpointer])

print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))
