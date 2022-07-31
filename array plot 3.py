

import matplotlib.pyplot as plt
import numpy as np
a=np.array([-1-4j,2+3j,3+2j,5+2j])
y=np.linspace(1,4,4,dtype=int)
print("values are:",a)
print("amplitude of values are:",abs(a))
plt.plot(y,abs(a))
#plt.bar(y,abs(a))
#plt.scatter(y,abs(a))
#plt.stem(y,abs(a))
#print angle
print("Angle=",np.angle(-1-4j,deg="True"))