import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()
a=np.array([4+4j,2-3j,3-1j,1+5j])
y=np.linspace(0,3,4,dtype=int)
x=abs(a)
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.2)
plt.subplot(2,2,1)
plt.plot(y,x)
plt.xlabel("X values")
plt.ylabel("Y values")

plt.subplot(2,2,2)
plt.bar(y,x)
plt.xlabel("X values")
plt.ylabel("Y values")

plt.subplot(2,2,3)
plt.scatter(y,x)
plt.xlabel("X values")
plt.ylabel("Y values")

plt.subplot(2,2,4)
plt.stem(y,x)
plt.xlabel("X values")
plt.ylabel("Y values")

