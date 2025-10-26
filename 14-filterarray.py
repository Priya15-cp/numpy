#filter:- getting some elements out of an array and createing a new array is called filtering
#A boolean index list is a list of boolean corresponding to indexes in the array(ture amd false)

# in boolean method it gives true value bu default ignor false value lets take an example
import numpy as np
sa=np.array([23,45,67,89])
sa1=[True,False,True,True]
sa2=sa[sa1]#matcing array means we are alining element of sa array witrh booleaN VALUES
print(sa2)

#now we create filter array
import numpy as np
sa=np.array([23,45,67,89])
newsa=[]
for i in sa:
    if(i>23):
        newsa.append(True)
    else:
        newsa.append(False)
sa1=sa[newsa]#index matching
print(newsa)
print(sa1)


#we can also do above problem without using if-else
import numpy as np
sa=np.array([23,45,67,89])

newsa=sa>23
sa1=sa[newsa]#index matching
print(newsa)
print(sa1)

