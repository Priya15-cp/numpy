#it estimates how many times an event occures
#parameteres of poisson - lam(number of occurance or rate) , size
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sa=random.poisson(lam=3,size=10)
print(sa)
sns.kdeplot(random.poisson(sa))
plt.show()

