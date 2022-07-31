import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.01)#start,stop,step
y=np.sin(x)
z=np.cos(x)
dy=np.gradient(y)
plt.plot(x,y,x,dy)
plt.xlabel('x values from 0 to 10')
plt.ylabel('sin(x) and d(sin(x))')
plt.title('Plot of SINE and Derivative of SINE from 0 to 10')
plt.legend(['sin(x)','d(sin(x))'])
plt.show()





