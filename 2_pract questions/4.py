# Create: (a) an array of five zeros, (b) a 2 × 4 array of ones, (c) a 4 × 4 identity matrix, and (d) all even numbers from 2 to 20 using arange(). Print each result.

import numpy as np

a = np.zeros(5)

b =np.ones([2,4])

c= np.eye(4,4)

d=np.arange(2,22,2)

print(a) #[0. 0. 0. 0. 0.]

print(b) #[[1. 1. 1. 1.]
      #      [1. 1. 1. 1.]]

print(c) #

'''[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]'''


print(d) #[ 2  4  6  8 10 12 14 16 18 20]