import numpy as np

array = np.array([x**2 for x in range(10)], dtype=float)

print(array)
print(f"차원 수 : {array.ndim}")
print(f"모양 : {array.shape}")
print(f"크기 : {array.size}")
print(f"타입 : {array.dtype}")

# array type 변경
array = array.astype(int)
print(array)

matrix = np.arange(8).reshape((2, 4))
print(matrix)

# Q1. sum 함수로 matrix의 총 합계를 구해 출력해보세요.
print(np.sum(matrix))

# Q2. max 함수로 matrix 중 최댓값을 구해 출력해보세요.
print(np.max(matrix))

# Q3. min 함수로 matrix 중 최솟값을 구해 출력해보세요.
print(np.min(matrix))

# Q4. mean 함수로 matrix의 평균값을 구해 출력해보세요.
print(np.mean(matrix))

# Q5. sum 함수의 axis 매개변수로 각 열의 합을 구해 출력해보세요.
print(np.sum(matrix, axis=0))

# Q6. sum 함수의 axis 매개변수로 각 행의 합을 구해 출력해보세요.
print(np.sum(matrix, axis=1))

# Q7. std 함수로 matrix의 표준편차를 구해 출력해보세요.
print(np.std(matrix))

# Q8. 마스킹 연산을 이용하여 matrix 중 5보다 작은 수들만 추출하여 출력해보세요.
print(matrix[matrix < 5])