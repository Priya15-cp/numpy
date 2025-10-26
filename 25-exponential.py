#it is used for describing the time till the next event that is like failure and sucess
#parameter:-scale()

import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
sa=random.exponential(scale=3,size=(2,3))
print(sa)

sns.kdeplot(sa)
plt.show()