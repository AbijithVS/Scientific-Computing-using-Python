
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.01)
fig,ax=plt.subplots(2)
y=np.sin(x)
dy=np.gradient(y)
z=np.cos(x)
dz=np.gradient(z)
ax[0].plot(x,dy,'b',label="d((sin(x))")
ax[1].plot(x,dz,'--r',label="d(cosine(x))")

ax[0].legend(loc="upper right")
ax[1].legend(loc="upper right")

