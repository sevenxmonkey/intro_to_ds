import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)

y = np.array([4, 5, 6])

m = np.array([[7,8,9],[10,11,12]])
m_shape = m.shape

# Arange returns evenly spaced values within a given interval.
n = np.arange(0, 30, 2)
# print(n)

# reshape returns an array with the same data with a new shape
n = n.reshape(3, 5)
# print(n)

# linspace returns evenly spaced numbers over a specified interval
o = np.linspace(0, 4, 9)
# print(o)

# resize changes the shape and size of array in-place
o.resize(3, 3)
# print(o)

# ones return a new array of given shape and type, filled with ONE(s).
one = np.ones((3,2))
# print(one)

# zeros returns a new array of given shape and type, filled with ZERO(s).
zero = np.zeros((2,3))
# print(zero)

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
ey = np.eye(3)
# print(ey)

# diag extracts a diagonal or construxts a diagonal array.
dia = np.diag(y)
# print(dia)

# Create an array using repeating list (or see np.tile)
reap = np.array([1,2,3]*3)
# print(reap)

# Reapeate elements of an array using repeat
re = np.repeat([1, 2, 3], 3)
# print(re)


#Combining Arrays
p = np.ones([2, 3], int)
vst = np.vstack([p, 2*p]) # using vstack to stack arrays in sequence vertically
# print(vst)
hst = np.hstack([p, 2*p]) # using hstack to stack arrays in sequence horizontally
# print (hst)

print(['a', 'b', 'c'] + [1, 2, 3])



