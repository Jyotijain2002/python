import numpy as np

x=np.array([[0.5,1.5],[1,1],[1.5,.5],[3,.5],[2,2],[1,2.5]])
y=np.array([0,0,0,1,1,1])


from sklearn.linear_model import LogisticRegression

lr_model=LogisticRegression()
# fit the model:  You can fit this model on the training data by calling fit function.
lr_model.fit(x,y)

#make prediction: 
y_pred=lr_model.predict([[2,3],[4,5]])

print("Prediction on training set:", y_pred)

#calculate accuracy
print('accuracy on training set:',lr_model.score(x,y))
