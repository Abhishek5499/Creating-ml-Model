# Create a Python list [1, 2, 3, 4] and print list * 2. Then create the same values as a NumPy array and print array * 2. 
# Write one sentence explaining why the outputs are different.

import numpy as np

l1 = [1,2,3,4]
print(l1*2)

"""
out put :- [1, 2, 3, 4, 1, 2, 3, 4]"""

num=np.array([1,2,3,4])

print(num*2)
'''

output :- [2 4 6 8]'''



"""
A Python list * 2 repeats the list twice, while a NumPy array * 2 performs element-wise multiplication on every element."""


"""Key point: Python lists use * for repetition, whereas NumPy arrays use * for mathematical multiplication."""