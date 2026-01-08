import numpy as np
attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]

# functions
# sum,max,min,avg
# axis =0 // column
# axis =1 // row

arr = np.array(attendance)

#dispay student wise present count
print(np.sum(arr,axis=1))

#display day wise present count
print(np.sum(arr,axis=0))

# update student10 tuesday attendance as present
arr[9,1] = 1
print(arr)

#display student wise absent count
studentwise_absent = np.count_nonzero(arr==0,axis=1)
print(studentwise_absent)

#display day wise absent count
daywise_absent = np.count_nonzero(arr==0,axis=0)
print(daywise_absent)

