import numpy as np
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
print("Enter the number in a single line separated by space:")
val = list(map(int, input().split()))
matrix = np.array(val).reshape(a,b)
print(matrix)
# trying that once again