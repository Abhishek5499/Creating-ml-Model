# Create a 3 × 3 NumPy array containing the numbers 1 to 9. 
# Print the complete array, the element at row 2 column 3, and the last element using negative indexing..

import numpy as np

a1 = np.array([[1,2,3,],
                [4,5,6],
                [7,8,9]])

print(a1)
# print(a1.ndim)
# print(a1.shape)
# print(a1.size)


print(f'Row2,column3 :',a1[1,2])

print(f'negative indexing :',a1[-1,])