import numpy as np

prices = np.array([100,120,140,550,76])

discount_prices = prices - 10
print(discount_prices)

new_price = prices + 20
print(new_price)

arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [10,11]
])

print(arr1+arr2)