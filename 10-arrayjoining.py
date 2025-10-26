#joining of array for this we use concatenate() function

#joining the 1-D array

import numpy as np
sa=np.array([1,2,3,4])
sa1=np.array([5,6,7])
sa2=np.concatenate((sa,sa1))
print(sa2)

#joining the 2-d array
import numpy as np
sa=np.array([[1,2,3],[3,4,5]])
sa1=np.array([[4,5,6],[5,7,8]])
sa2=np.concatenate((sa,sa1),axis=1)#when we include axis it combonr array as same index in both array like 0 index array
 #insa comncatenate with 0 index array of sa1
print(sa2)

#joining array using stack() function:it work on indexing
import numpy as np
sa=np.array([[1,2,3],[3,4,5]])
sa1=np.array([[4,5,7],[5,7,8]])
sa2=np.stack((sa,sa1),axis=1)
print(sa2)

#stack along with rows = hstack
import numpy as np
sa=np.array([[1,2,3],[3,4,5]])
sa1=np.array([[4,5,7],[5,7,8]])
sa2=np.hstack((sa,sa1))
print(sa2)

