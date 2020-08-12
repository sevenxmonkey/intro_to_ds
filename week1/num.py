import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)

y = np.array([4, 5, 6])

m = np.array([[7,8,9],[10,11,12]])
m_shape = m.shape

# Arange returns evenly spaced values within a given interval.
n = np.arange(0, 30, 2)
print(n)

# reshape returns an array with the same data with a new shape
n = n.reshape(3, 5)
print(n)

