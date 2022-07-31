# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:22:11 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.01)
fig,ax=plt.subplots(2)
ax[0].plot(x,np.sinh(x),'b',label="hyperbolic sine")
ax[1].plot(x,np.cosh(x),'--r',label="hyperbolic cosine")

ax[0].axis("equal")
ax[1].axis("equal")

ax[0].legend(loc="lower left");
ax[1].legend(loc="lower left");