#it is basically used as a basis to verify the hypothesis
#param:-df(degree of freedom),size
import matplotlib.pyplot as plt
import seaborn as  sns 
from numpy import random
sa=random.chisquare(df=2,size=(3,4))
print(sa)