# Create the following array and use slicing to print: the first row, the second column, the last two rows, and the middle 2 × 2 block
'''Array:
[[10, 20, 30, 40],
 [50, 60, 70, 80],
 [90,100,110,120]]
'''
import numpy as np

a1 = np.array(
[[10, 20, 30, 40],
 [50, 60, 70, 80],
 [90,100,110,120]]
)

print(a1[0,])
print(a1[:,1])
print(a1[1:3])

print(a1[1:3,1:3])
