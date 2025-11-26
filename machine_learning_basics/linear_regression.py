import numpy as np
import matplotlib.pyplot as plt

from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl


# x_train=np.array([19.03, 7.85, 33.14, 55.67, 72.93, 31.81, 74.05, 5.22, 17.58, 26.54, 88.08, 93.63, 62.11, 44.89, 78.41, 19.30, 4.70, 48.91, 79.54, 25.10, 89.26, 91.56, 1.83, 56.49, 14.28, 71.01, 6.77, 85.34, 49.62, 53.07, 43.19, 97.40, 29.87, 83.17, 3.51, 60.95, 38.22, 12.45, 99.19, 81.60, 50.33, 23.95, 94.75, 68.30, 10.72, 36.46, 58.78, 96.04, 76.13, 21.48, 47.90, 8.99, 65.52, 3.86, 70.15, 27.29, 9.42, 59.81, 41.05, 15.93, 86.84, 98.27, 2.11, 63.50, 39.73, 52.09, 77.36, 13.91, 34.66, 92.44, 46.21, 67.08, 20.55, 73.80, 54.38, 95.83, 30.69, 11.23, 80.01, 37.55, 61.96, 4.34, 28.60, 84.71, 75.25, 57.19, 16.70, 90.98, 45.03, 69.25, 22.88, 87.65, 35.00, 18.15, 6.09, 66.47, 40.07, 99.88])
# y_train=np.array([945.72, 53.08, 127.19, 888.63, 672.45, 301.99, 442.10, 81.36, 159.24, 733.51, 989.15, 621.84, 1.48, 203.77, 506.90, 853.47, 999.03, 11.20, 360.82, 792.65, 48.33, 245.00, 711.17, 333.39, 901.55, 14.61, 555.28, 609.91, 287.05, 780.20, 412.88, 977.34, 182.56, 5.09, 644.02, 390.11, 822.46, 51.67, 100.99, 467.50, 755.83, 22.18, 599.40, 930.29, 321.73, 10.50, 868.96, 439.85, 29.54, 770.07, 493.36, 60.14, 959.01, 177.22, 574.63, 701.38, 266.02, 911.75, 44.97, 833.60, 350.85, 190.41, 688.19, 99.80, 520.67, 230.93, 76.40, 400.05, 805.16, 582.78, 16.99, 319.42, 633.55, 148.06, 890.31, 377.92, 540.23, 110.66, 749.57, 421.30, 966.89, 72.58, 258.94, 666.60, 388.47, 920.01, 133.75, 840.10, 560.52, 219.04, 788.11, 477.86, 650.00, 30.70, 985.49, 150.12, 87.03, 700.32])

# print(len(x_train))
# print(len(y_train))
# # plt.scatter(x_train,y_train)

# # plt.title('House Price Prediction')
# # plt.xlabel('size in feet^2')
# # plt.ylabel("price in $1000's")
# # plt.show()


# def compute_model_output(x,w,b):
#     m=x.shape[0]
#     f_wb=np.zeros(m)
#     for i in range(m):
#         f_wb[i]=x[i]*w+b
#     return f_wb


# w=100
# b=100

# predicted_y=compute_model_output(x_train,w,b)

# #plot our model prediction:
# plt.plot(x_train,predicted_y,c='b',label="Our prediction")

# #plot actual data points:
# plt.scatter(x_train,y_train,marker='x',c='r',label="actual values")

# plt.title('House Price Prediction')
# plt.xlabel('size in feet^2')
# plt.ylabel("price in $1000's")
# plt.legend()
# plt.show()


def compute_cost(x, y, w, b): 
    """
    Computes the cost function for linear regression.
    
    Args:
      x (ndarray (m,)): Data, m examples 
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters  
    
    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    # number of training examples
    m = x.shape[0] 
    
    cost_sum = 0 
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum = cost_sum + cost  
    total_cost = (1 / (2 * m)) * cost_sum  

    return total_cost


x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
y_train = np.array([250, 300, 480,  430,   630, 730,])

plt_intuition(x_train,y_train)

plt.close('all') 
fig, ax, dyn_items = plt_stationary(x_train, y_train)
updater = plt_update_onclick(fig, ax, x_train, y_train, dyn_items)


soup_bowl()


        


