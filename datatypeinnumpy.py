import numpy as np
sa=np.array([1,2,3,4,5])
print(sa.dtype)

import numpy as np
sa=np.array([[1.2,2.3,3.4,4.5],[4.7,5.8,6.7,7.6]],dtype='i')
print(sa)
print(sa.dtype)

#boolen cant canged by this method then for boolen we use astype
import numpy as np
sa=np.array([1.1,2.1,3.1,0],dtype=bool)

print(sa)
print(sa.dtype)