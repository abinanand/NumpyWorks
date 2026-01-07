# numpy => numerical python
import numpy as np

array = np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])

print(array.ndim)
print(array.size)
print(array.shape)

# fetch 0th row
print(array[0])

# fetch 2th row
print(array[2])

# row slicing from 1 to 2
print(array[1:3])

# row slicing from 0 to 1
print(array[0:2])

# column slicing 
print(array[:,1:3])
print(array[:,1]) 
print(array[:,1:2]) 

print(array[::2]) #[start:stop:step]

print(array[2,1]) 
print(array[1:3,1:3])

