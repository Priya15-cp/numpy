#logistic distribution :- describe growth- it is basically important in regression and normal network
#param:- lac(mean=0),scale(sd=1),size
import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
sa=random.logistic(loc=1,scale=2,size=(2,3))
print(sa)
