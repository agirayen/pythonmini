import numpy as np

data= list(range(20,100,5))

q1 = np.quantile(data,0.25)
q2 = np.quantile(data,0.50)
q3 = np.quantile(data,0.75)

print("Quartile 1 : ",q1)
print("Quartile 2 : ",q2)
print("Quartile 3 : ",q3)

def quartiledeviation(a,b):
    return (a-b)/2
print(quartiledeviation(q3,q1))

