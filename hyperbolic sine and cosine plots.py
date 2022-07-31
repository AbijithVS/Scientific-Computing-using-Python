

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.01)
fig,ax=plt.subplots(2)
ax[0].plot(x,np.sinh(x),'b',label="hyperbolic sine")
ax[1].plot(x,np.cosh(x),'--r',label="hyperbolic cosine")

ax[0].legend(loc="upper left")
ax[1].legend(loc="upper left")

