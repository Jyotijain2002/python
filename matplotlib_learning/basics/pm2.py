import numpy as np
import matplotlib.pyplot as plt

x_train=np.array([1,2,3,4,5])
y_train=np.array([1,4,9,16,25])
z_train=np.array([1,8,27,64,125])

plt.plot(x_train,y_train,z_train)
plt.show()