# Create a NumPy array of marks: [35, 78, 92, 41, 67, 88, 29]. Print only the marks greater than or equal to 60. Also print the average, maximum and minimum marks.
# Hint: Use boolean filtering plus mean(), max() and min().


import numpy as np

marks =np.array([35, 78, 92, 41, 67, 88, 29])

print(marks>=60) #[False  True  True False  True  True False]

passed = marks[marks>=60]

print(passed) #[78 92 67 88]

print(marks.mean())# 61.42857142857143
print(marks.max())# 92
print(marks.min()) #29