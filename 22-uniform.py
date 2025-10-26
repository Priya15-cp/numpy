#uniform distribution:- it only made for probability (p)
#parameter:- there arae 3  param a,b,size : a means lower bound its default value is  0.1 and a is upper bound its default value is 1.0,size
import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
import numpy as np
sa=random.uniform(size=4)
print(sa)

sns.kdeplot(sa)
plt.show()

