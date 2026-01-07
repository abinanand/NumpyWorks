import numpy as np

lst = [10,20,30,40,50,60]
#       0, 1, 2, 3, 4, 5
arr = np.array(lst)

# fetching a specific element

print(arr[3]) #40

# slicing arr[start:stop] NB:end excluded

print(arr[1:4]) #[20 30 40]
print(arr[3:6]) #[40 50 60]
