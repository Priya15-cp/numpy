#multinomial Distribution :- it os a generalization of binomial distribution
#param:-there are three parameters n,pvals(),size
#n=number of possibility or outcome 
#pvals()=means list of posibility and output
#size=shape of retured array
import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
sa=random.multinomial(n=4,pvals=[1/6,1/6,1/6,1/6],size=3)
print(sa)
sns.kdeplot(sa)
plt.show()
#multinomial samples will not produce a single value , they will produce one value for each pvals