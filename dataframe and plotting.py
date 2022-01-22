import pandas as p
import matplotlib.pyplot as plt
import numpy as np

data=p.read_excel('SCL work.xlsx')
data2=data[2]
print(data2) 


m=np.mean(data2)
print("MEAN:",m)
s=np.std(data2)
print("STANDARD DEVIATION:",s)
v=np.cov(data2)
print("CO-VARIANCE:",v)


plt.subplot(2,2,1)
plt.bar(data2)
plt.xlabel("number")
plt.ylabel("random")
plt.subplot(2,2,2)
plt.stem(data2)
plt.xlabel("number")
plt.ylabel("random")
plt.subplot(2,2,3)
plt.plot(data2)
plt.xlabel("number")
plt.ylabel("random")
plt.subplot(2,2,4)
plt.scatter(data2)
plt.xlabel("number")
plt.ylabel("random")



