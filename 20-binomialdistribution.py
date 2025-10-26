import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random
import numpy as np
sa=np.random.binomial(n=10,p=0.5,size=10)
print(sa)

#visual representation
sns.kdeplot(x=sa)
plt.show()