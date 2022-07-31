
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.01)
fig,ax=plt.subplots(2)
y=np.sinh(x)
dy=np.gradient(y)
z=np.cosh(x)
dz=np.gradient(z)
ax[0].plot(x,dy,'b',label="d((sinh(x))")
ax[1].plot(x,dz,'--r',label="d(cosh(x))")

ax[0].legend(loc="upper left")
ax[1].legend(loc="upper left")

