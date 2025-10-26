#iterating array;-going through the all element one by one or like a loop

# iteartion in 1-D array 

import numpy as np
sa=np.array([1,2,3,4,5,6])
for i in sa:
    print(i)

#iteration in 2-d array
import numpy as np 
num=np.array([[1,2,3,4],[5,6,7,8]])
for i in num:
    print(i)#inly iterate array inside 2-d
    #for iterating element inside these array
    for a in i:
        print(a)


#iteration in 3-d aray
import numpy as np
saa=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in saa:
    print(i)#it goes inside 1st dimention
    for a in i:
        print(a)#it goes inside 2nd dimension
        for b in a:
            print(b)#this goes inside last dimention and print elements of of arrays


#nditer makes it easy to iterate like we can iterate without using loop
import numpy as np
sa=np.array([1,2,3,4,5])
for i in np.nditer(sa):
    print(i)

import numpy as np
saa=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in np.nditer(saa):#it directly acces element
    print(i)


#by using nditer funstion we can also iterate with differnt step size 
import numpy as np
saa=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in np.nditer(saa[ 0:2,::3]):
    print(i)#
