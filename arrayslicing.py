#slicing in 1-D
import numpy as np
sa=np.array([1,2,3,4,5,6])
print(sa[0:4:2])

#slicing in 2-d
import numpy as np
sa=np.array([[1,2,3,4],[5,6,7,8]])
print(sa[1,0:4])
print(sa[0:2,1:3])

#slicing in 3-d array
import numpy as np
sa=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[2,3,4]]])
print(sa[1,0,0:3])