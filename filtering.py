import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

print(productivity[productivity<8])

# working hours between 5 to 7

print (productivity [(productivity>5) & (productivity<=7)])

# print working hous of first employee with working hrs <8

first_employee = productivity[:,0]
print(first_employee)

print(first_employee[first_employee<8])

# print last two employees working hrs <7

last_employees = productivity[:,8:]
print(last_employees)

print(last_employees[last_employees<7])

# change hrs <7 into 0
productivity[productivity<8]=0
print(productivity)

