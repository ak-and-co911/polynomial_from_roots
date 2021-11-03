import numpy as np
# create a sample array
arr = np.array([[1,1,1],[2,2,2]])
values = np.array([3,4]).reshape(2,1)
# append values to arr
new_arr = np.append(arr, values, axis=1)
# print
print("Original array:\n", arr)
print("Appended Array:\n", new_arr)