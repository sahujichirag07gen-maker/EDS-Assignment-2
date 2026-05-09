# 3.1.1 Numpy array operations 
import numpy as np

# write your code here...
r,c=map(int,input().split())
data=[]
for i in range(r):
	row= list(map(int,input().split()))
	data.append(row)
arr = np.array(data).reshape(r,c)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)