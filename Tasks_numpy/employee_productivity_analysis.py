import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

#1. Calculate the total number of hours worked by each employee over 10 days.
total_hours = np.sum(productivity,axis=1)
print(total_hours)

#2. Calculate the total work hours for each day across all employees.
total_work_eachday = np.sum(productivity,axis=0)
print(total_work_eachday)

#3. Find the average working hours per employee.
average_hours_employee = np.average(productivity,axis=1)
print(average_hours_employee)

#4. Find the average working hours per day.
average_hours_per_day = np.average(productivity,axis=0)
print(average_hours_per_day)

#5. Identify the employee index who worked the maximum total hours.
print(np.argmax(total_hours))

#6. Identify the employee index who worked the minimum total hours.
print(np.argmin(total_hours))

#7. Find the day index with the highest total working hours.
print(np.argmax(total_work_eachday))

#8. Identify employees who are overworked if average hours exceed 8 per day.
print(np.where(average_hours_employee>8))

#9. Calculate the difference between the most productive and least productive employee.
productivity_difference = np.max(total_hours) - np.min(total_hours)
print(productivity_difference)