import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from plt_one_addpt_onclick import plt_one_addpt_onclick
from lab_utils_common import draw_vthresh


'''
sigmoid/ logistic function:

g(z)=1/(1+e^(-z))

NumPy has a function called [`exp()`], which offers a convenient way to calculate the exponential ( $e^{z}$) of all elements in the input array (`z`).
 It also works with a single number as an input, as shown below.
'''
input_array=np.array([1,2,3])
exp_array=np.exp(input_array)

print(f"input-array: {input_array}")
print(f'exp-array: {exp_array}')



def sigmoid(z):

    g=1/(1+np.exp(-z))
    return g

z_tmp=np.arange(-10,11)
y=sigmoid(z_tmp)

np.set_printoptions(precision=3)
print('input(z), output(sigmoid(z))')
print(np.c_[z_tmp,y])

fig,ax=plt.subplots(1,1,figsize=(5,3))

ax.set_title("sigmoid function")
ax.set_ylabel('sigmoid(z)')
ax.set_xlabel('z')
plt.plot(z_tmp,y)
draw_vthresh(ax,0)
plt.show()


x_train=np.array([0.,1,2,3,4,5])
y_train=np.array([0,0,0,1,1,1])

w_in=np.zeros((1))
b_in=0

plt.close('all')
addpt=plt_one_addpt_onclick(x_train,y_train,w_in,b_in,logistic=True)
plt.show()