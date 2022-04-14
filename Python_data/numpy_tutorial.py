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
