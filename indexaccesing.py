
#accesing element in array by using index in 1-D
import numpy as np 
x=np.array([3,5,6,7])
print(x[2])

#2-D array accessing by index - in this you give row and then we give the index of element that we want to access
import numpy as np
sa=np.array([[1,2,3,4],[5,6,7,8]])
print("1st elemrnt of 2nd row",sa[1,0])


#3-D array accesing using index
import numpy as np
y=np.array([[[1,2,3],[4,5,6]],[[4,3,5],[8,6,5]]])
print("2nd array inside that also 2nd array and its 2nd element",y[1,1,1])