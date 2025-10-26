#it is used in signal processing 
#parem- scale(default=0.1),size
import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
sa=random.rayleigh(scale=2,size=(2,3))
print(sa)
sns.kdeplot(sa)
plt.show()