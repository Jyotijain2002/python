import numpy as np
import matplotlib.pyplot as plt
from lab_utils_multi import load_house_data,run_gradient_descent
from lab_utils_multi import norm_plot,plt_equal_scale,plot_cost_i_w
from lab_utils_common import dlc

x_train,y_train=load_house_data()
x_features=['size(sqft)','bedrooms','floors','age']


fig,ax=plt.subplots(1,4,figsize=(12,3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(x_train[:,i],y_train)
    ax[i].set_xlabel(x_features[i])

ax[0].set_ylabel("price(1000's)")
plt.show()

'''
we can see that
in plot:
with house size the price is generally increasing and with age it is 
generally decreasing
and with #bedrooms and floors we are not seeing any specific kind of
pattern
'''
_,_,hist=run_gradient_descent(x_train,y_train,10,alpha=9.9e-7)
#here the learning rate is too high ,the solution does not converge

plot_cost_i_w(x_train,y_train,hist)
'''
The plot on the right shows the value of one of the parameters,  𝑤0
 . At each iteration, it is overshooting the optimal value and as a result, cost ends up increasing rather than approaching the minimum. Note that this is not a completely accurate picture as there are 4 parameters being modified each pass rather than just one. This plot is only showing  𝑤0
  with the other parameters fixed at benign values. In this and later plots you may notice the blue and orange lines being slightly off.
'''

_,_,hist=run_gradient_descent(x_train,y_train,10,alpha=9e-7)
plot_cost_i_w(x_train,y_train,hist)
'''
On the left, you see that cost is decreasing as it should. On the right, you can see that  𝑤0
  is still oscillating around the minimum, but the cost is decreasing with every iteration rather than increasing. Note above that dj_dw[0] changes sign with each iteration as w[0] jumps over the optimal value. This alpha value will converge. You can vary the number of iterations to see how it behaves.
'''

# lets try more smaller value of alpha
_,_,hist=run_gradient_descent(x_train,y_train,10,alpha=1e-7)
plot_cost_i_w(x_train,y_train,hist)
'''
On the left, you see that cost is decreasing as it should. On the right, you can see that  w0
  is approaching the minimum without oscillations. dj_w0 is negative throughout the run. This solution will also converge.
'''

#feature scaling
# z-score normalization
def zscore_normalize_features(x):
    #x->np array
    #mean
    mu=np.mean(x)
    #standard deviation
    sigma=np.std(x)
    x_norm=(x-mu)/sigma

    return (x_norm,mu,sigma)

mu     = np.mean(x_train,axis=0)   
sigma  = np.std(x_train,axis=0) 
X_mean = (x_train - mu)
X_norm = (x_train - mu)/sigma      

fig,ax=plt.subplots(1, 3, figsize=(12, 3))
ax[0].scatter(x_train[:,0], x_train[:,3])
ax[0].set_xlabel(x_features[0]); ax[0].set_ylabel(x_features[3])
ax[0].set_title("unnormalized")
ax[0].axis('equal')

ax[1].scatter(X_mean[:,0], X_mean[:,3])
ax[1].set_xlabel(x_features[0]); ax[0].set_ylabel(x_features[3])
ax[1].set_title(r"X - $\mu$")
ax[1].axis('equal')

ax[2].scatter(X_norm[:,0], X_norm[:,3])
ax[2].set_xlabel(x_features[0]); ax[0].set_ylabel(x_features[3])
ax[2].set_title(r"Z-score normalized")
ax[2].axis('equal')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.suptitle("distribution of features before, during, after normalization")
plt.show()
'''
The plot above shows the relationship between two of the training set parameters, "age" and "size(sqft)". These are plotted with equal scale.

Left: Unnormalized: The range of values or the variance of the 'size(sqft)' feature is much larger than that of age
Middle: The first step removes the mean or average value from each feature. This leaves features that are centered around zero. It's difficult to see the difference for the 'age' feature, but 'size(sqft)' is clearly around zero.
Right: The second step divides by the standard deviation. This leaves both features centered at zero with a similar scale.
'''


# normalize the original features
X_norm, X_mu, X_sigma = zscore_normalize_features(x_train)
print(f"X_mu = {X_mu}, \nX_sigma = {X_sigma}")
print(f"Peak to Peak range by column in Raw        X:{np.ptp(x_train,axis=0)}")   
print(f"Peak to Peak range by column in Normalized X:{np.ptp(X_norm,axis=0)}")
'''
peak to peak value of a column: (max-min) for that column
The peak to peak range of each column is reduced from a factor of thousands to a factor of 2-3 by normalization.

axis 0: moves down the row
axis 1: moves across column

'''

fig,ax=plt.subplots(1, 4, figsize=(12, 3))
for i in range(len(ax)):
    norm_plot(ax[i],x_train[:,i],)
    ax[i].set_xlabel(x_features[i])
ax[0].set_ylabel("count");
fig.suptitle("distribution of features before normalization")
plt.show()
fig,ax=plt.subplots(1,4,figsize=(12,3))
for i in range(len(ax)):
    norm_plot(ax[i],X_norm[:,i],)
    ax[i].set_xlabel(x_features[i])
ax[0].set_ylabel("count"); 
fig.suptitle("distribution of features after normalization")

plt.show()
'''
Notice, above, the range of the normalized data (x-axis) is centered around zero and roughly +/- 2. Most importantly, the range is similar for each feature.
'''

# let re-run gradient descent algo with larger alpha, this will speed up gradient descent

w_norm,b_norm,hist=run_gradient_descent(X_norm,y_train,1000,1.0e-1)
plot_cost_i_w(X_norm,y_train,hist) 
'''
The scaled features get very accurate results much, much faster!. Notice the gradient of each parameter is tiny by the end of this fairly short run. A learning rate of 0.1 is a good start for regression with normalized features. 
'''

#predict target using normalized features
m = X_norm.shape[0]
yp = np.zeros(m)
for i in range(m):
    yp[i] = np.dot(X_norm[i], w_norm) + b_norm

    # plot predictions and targets versus original features    
fig,ax=plt.subplots(1,4,figsize=(12, 3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(x_train[:,i],y_train, label = 'target')
    ax[i].set_xlabel(x_features[i])
    ax[i].scatter(x_train[:,i],yp,color=dlc["dlorange"], label = 'predict')
ax[0].set_ylabel("Price"); ax[0].legend();
fig.suptitle("target versus prediction using z-score normalized model")
plt.show()

'''
The results look good. A few points to note:

with multiple features, we can no longer have a single plot showing results versus features.
when generating the plot, the normalized features were used. Any predictions using the parameters learned from a normalized training set must also be normalized.
'''

'''
Prediction The point of generating our model is to use it to predict housing prices that are not in the data set. Let's predict the price of a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old. Recall, that you must normalize the data with the mean and standard deviation derived when the training data was normalized.
'''

x_house=np.array([1200,3,1,40])
x_house_norm=(x_house-X_mu)/X_sigma
print(x_house_norm)
x_house_predict=np.dot(x_house_norm,w_norm)+b_norm
print(f" predicted price of a house with 1200 sqft, 3 bedrooms, 1 floor, 40 years old = ${x_house_predict*1000:0.0f}")

plt_equal_scale(x_train,X_norm,y_train)