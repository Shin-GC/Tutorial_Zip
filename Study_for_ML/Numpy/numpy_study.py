import numpy as np
#1차원 배열
list_normal=[1,2,3]

print(type(list_normal))
print(f'list_normal:{list_normal}\n')

arr=np.array(list_normal)
print(type(arr))
print(f'np.array:{arr}\n')

#2차원 배열 =매트릭스
mat=[[1,2],[3,4]]
print(type(mat))
print(f'mat:{mat}\n')
mat_arr=np.array(mat)
print(type(mat_arr))
print(f'np.array\n{mat_arr}\n')
zeros=np.zeros(2)
zeros_mat=np.zeros((2,2))
print(type(zeros))
print(f'np.zeros\n{zeros}\n')
print(type(zeros_mat))
print(f'np.zeros_mat\n{zeros_mat}\n')
ones=np.ones(2)
ones_mat=np.ones((2,2))
print(type(ones))
print(f'np.ones\n{ones}\n')
print(type(ones_mat))
print(f'np.ones_mat\n{ones_mat}\n')

arange=np.arange(1,11)
#1부터 10까지 간격 1을 가진 배열
print(type(arange))
print(f'np.arange(1,11)\n{arange}\n')

arange2=np.arange(1,11,2)
#1부터 10까지 간격 2를 가진 배열
print(type(arange2))
print(f'np.arange2(1,11)\n{arange2}\n')

random=np.random.rand(3,3)
#0과 1 범위 내의 연속 균등 분포(Uniform)에서 랜덤 값을 가져와 배열 생성
print(type(random))
print(f'np.random.rand(3,3):\n{random}\n')

random_standard=np.random.randn(3,3) 
## 0과 1범위 내의 정규 분포(standard normal)에서 랜덤으로 값을 가져와 생성
print(type(random_standard))
print(f'np.random.randn(3,3)\n{random_standard}\n')

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(f'arr.shape:{arr.shape}\n')
#배열 모양을 확인 [x.shape()]
#배열 모양은 row[세로],col[가로] 형태로 표현됩니다.

print(f'dtype{arr.dtype}\n')
#배열 내의 자료형 표현 x.dtype

print(f'reshape\n{arr.reshape(2,3)}')
#배열 모양 변경 reshape

arr=arr.astype(float)
#배열 데이터 타입 변경 (int -> float)

print(f'astype(float):{arr.dtype}')

arr1=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
arr2=np.zeros(3)
arr3=np.ones(3)

print('arr1\n',arr1,'\narr2\n',arr2,'\narr3\n',arr3)

con=np.concatenate((arr2,arr3),axis=0)
#row[가로] 기준으로 합치기
#배열 합치기 np.concatenate()
print('con\n',con)
print(f'con.shape:{con.shape}')

con=con.reshape(6,1)
#col 기준으로 합치기 위해 모양 변경
print(con)

rst = np.concatenate((arr1, con), axis=1)
#col 기준으로 합치기
#col의 길이가 같아야함
print(rst)

col_del=rst[:,0:2]
#특정 col 잘라내기
print('col_del\n',col_del)

row_del=rst[1:,:]
print('row_del\n',row_del)