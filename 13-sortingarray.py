#sorting:-arranging in a order
import numpy as np
sa=np.array([8,5,6,7,2,3,1])
print(np.sort(sa))

#sorting of alphabste
import numpy as np
sa=np.array(['banana','apple','orange','kiwi'])
print(np.sort(sa))

import numpy as np
sa=np.array([True,False,True,True])
print(np.sort(sa))


#sorting in 2-D array
import numpy as np
sa=np.array([[1,4,5,6],[9,6,3,6]])
sa1=np.hstack(sa)
print(sa1)
print(np.sort(sa1))
