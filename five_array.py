import numpy as np

five_array = np.full((5,5),4)
#print(five_array)

ones_array = np.ones((3,3),dtype="int16")
#print(ones_array)

ones_array[1,1] = 100
#print(ones_array)

five_array[1:4,1:4] = ones_array

print(five_array)