# Write a program to read five integer values from the user, 
# store them first in a Python list, convert that list to a NumPy array, and then print array + 10.


import numpy as np

num = input("Enter 5 numbers: ")

l1 = list(map(int, num.split()))

print("Python list:", l1)

np_arr = np.array(l1)

print("NumPy array + 10:", np_arr + 10)


# out put :- 
'''
Enter 5 numbers: 1 2 3 4 5
Python list: [1, 2, 3, 4, 5]
NumPy array + 10: [11 12 13 14 15]
'''


