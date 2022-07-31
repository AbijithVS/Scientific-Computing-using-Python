import matplotlib.pyplot as plt
import numpy as np
a=np.array([1-5j,3+3j,6+2j,5+2j])
y=np.linspace(1,4,4,dtype=int)
print("values are:",a)
print("amplitude of values are:",abs(a))
plt.xlabel("Values")
plt.ylabel("Amplitude")
plt.title("Plot between values and their Amplitudes")
plt.plot(y,abs(a))
# plt.bar(y,abs(a))
# plt.scatter(y,abs(a))
# plt.stem(y,abs(a))
print("Angle=",np.angle(1-5j,deg="True"))




