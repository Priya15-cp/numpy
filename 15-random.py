#Random meaning:-something that cann't be predicted logically

from numpy  import random
sa=random.randint(100)#it givses random value between 0 to 100
print(sa)

#for float number :- it gives value between 0 to 1
from numpy import random
sa=random.rand()
print(sa)

#we can also generATE random array 
#we will generate 1-D array containing 5 random int from 0 to 100
from numpy  import random
sa=random.randint(100,size=(5))#it givses random value between 0 to 100
print(sa)

#also genrate 2-D array woth 3 rows each rows contain 5 elements form 0 tttto 100
from numpy  import random
sa=random.randint(100,size=(3,5))#it givses random value between 0 to 100
print(sa)

#for float:- array having 5 element
from numpy import random
sa=random.rand(5)
print(sa)

# we can also generate number from an given arry for 1-d
from numpy import random
sa=random.choice([1,6,5,4,3,2,6,5],size=(5))
print(sa)

#for 2-D
from numpy import random
sa=random.choice([1,6,5,4,3,2,6,5],size=(2,5))
print(sa)