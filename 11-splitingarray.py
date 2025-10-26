#spliting:- it is reverse of array and breaking of array
import numpy as np
sa=np.array([1,2,3,4,5,6])
sa1=np.array_split(sa,3)
print(sa1)
#what happewn if we divide this array in 6 differnt array

import numpy as np
sa=np.array([1,2,3,4,5,6])
sa1=np.array_split(sa,6)
print(sa1)

#we also can access spliting array by indexing
import numpy as np
saa=np.array([1,2,3,4,5,6])
sa1=np.array_split(saa,3)
print(sa1[0])

#spliting tge 2D into three 2-Dalong with rows
import numpy as np
sa=np.array([[1,2,3],[4,5,6],[7,8,9]])
sa1=np.array_split(sa,2,axis=1)
print(sa1)#it combine array of same index in differnt array

#alternative solution
import numpy as np
sa=np.array([[1,2,3],[4,5,6],[7,8,9]])
sa1=np.hsplit(sa,3)
print(sa1)
