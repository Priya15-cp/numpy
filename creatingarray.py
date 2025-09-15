import numpy as np #improting numpy

x=np.array([1,2,3,6,7,4,5])
print(x)
print(type(x))

a=np.array(45) #0-demention array
print(a.ndim)

a=np.array([1,2,3,4,5])
print(a.ndim)

a=np.array([[1,2,3,4],[6,7,8,9]])
print(a.ndim)

a=np.array([1,2,3,4],ndmin=3)
print(a)
print(a.ndim)

a=np.array([1,2,3,4],ndmin=5)
print(a)
print(a.ndim)

a=np.array([1,2,3,4],ndmin=10)
print(a)
print(a.ndim)