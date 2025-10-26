#searching array:-we can search on array for s certain value and returnthe indexes that get the match ny using where 
import numpy as np
sa=np.array([1,2,3,4,5,6])
sa1=np.where(sa==4)#it gives index whwre 4 lies
print(sa1)

#finding index where the element are even
import numpy as np
sa=np.array([1,2,3,4,4,5,5,6])
sa1=np.where(sa%2==0)
print(sa1)

#finding odd number
import numpy as np
sa=np.array([1,2,3,4,4,5,5,6])
sa1=np.where(sa%2==1)
print(sa1)


#Searchsort()-perform binary search in array and return index
import numpy as np
sa=np.array([1,6,7,8,4])
sa1=np.searchsorted(sa,2)#it gives us a index where 2 can be incerted in array
print(sa1)

#we can search by both side (left or right)by default it is seach from left
import numpy as np
sa=np.array([1,6,7,8,4])
sa1=np.searchsorted(sa,2,side='right')
print(sa1)

#how to access multiple value
import numpy as np
sa=np.array([1,3,5,7])
sa1=np.searchsorted(sa,[2,4,6])
print(sa1)