import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random
sa=random.normal(loc=1,scale=2,size=(2,3))
print(sa)
#for representing thr normal curve
sns.displot(random.normal(loc=1,scale=1,size=(2,3)))
plt.show()
