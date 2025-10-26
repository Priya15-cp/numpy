import numpy as np
sa=np.array([1,2,3,4,5,6])
print(sa.shape)
sa1=sa.reshape(2,3)
sa2=sa.reshape(3,2)
print(sa1)
print(sa2)


import numpy as np
sa=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sa1=sa.reshape(2,2,3)
print(sa1)


#flatering the array by converting multi-dimenstional array into 1-D

import numpy as np
sa=np.array([[[[[1,2,3,4]]]]])
print(sa.ndim)
sa1=sa.reshape(-1)
print(sa1.ndim)
