import numpy as np
from numpy import random
sa=np.array([4,5,2,7])
random.shuffle(sa)
print(sa)
#it made change on original array
#shuffle is the default version of random

import numpy as np
from numpy import random
sa=np.array([4,5,2,7])
sa1=random.permutation(sa)
print(sa1)

#permutation() fumction leave the original array unchanged