# array creation methods

    #np.array((Row,Column))
    #np.zeros((Row,Column))
    #np.ones((Row,Column))
    #np.full((Row,Column),value)
    #np.random.rand(Row,Column)
    #np.random.randint(low,high,(Row,Column))

import numpy as np

zeros_array = np.zeros((3,3),dtype="int16")
print(zeros_array)

ones_array = np.ones((4,4),dtype="int16")
print(ones_array)

full_array = np.full((6,7),7)
print(full_array)

random_array = np.random.rand(2,3)
print(random_array)

randint_array = np.random.randint(10,20,(3,3))
print(randint_array)



