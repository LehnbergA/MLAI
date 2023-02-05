# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:12:11 2022

@author: MNBE
"""

import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
X_data=np.array([[1,1],[2,1],[3,1],[4,1],[5,1],[10,1]])
Y_data=np.array([2,1,4,4,5,10])
beta_hat = np.linalg.inv(X_data.T.dot(X_data)).dot(X_data.T).dot(Y_data)
yhat = X_data.dot(beta_hat)
# plot data and predictions
plt.scatter(X_data[:,0], Y_data)
plt.plot(X_data[:,0], yhat, color='red')