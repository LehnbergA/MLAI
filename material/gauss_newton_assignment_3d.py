# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:13:53 2022

@author: dokto
"""
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
ax = plt.axes(projection='3d')


x = np.array([0,1,2,3,4])
y = np.array([0,1,2,3,4])
Xs, Ys = np.meshgrid(x, y)
Zs=np.array([[  0,   0,   0,   0,   0],
       [  0,  11,  20,  27,  32],
       [  0,  20,  32,  36,  32],
       [  0,  27,  36,  27,   0],
       [  0,  32,  32,   0, -64]])

X=Xs.flatten() 
Y=Ys.flatten()
#Z=(12*X*Y-(X**2)*(Y**2))+ 10 * np.random.randn(25)
Z=Zs.flatten()+ 10 * np.random.randn(25)
#Zs=(12*Xs*Ys-(Xs**2)*(Ys**2))+ 10 * np.random.randn(5,5)
Zs=Zs+ 10 * np.random.randn(5,5)
#ax.scatter3D(X, Y, Z);
surf = ax.scatter3D(Xs, Ys, Zs,color='red')


P0=[1,1,1,1]
J=np.zeros([len(X),len(P0)])
Iter=0
while True:
    Iter+=1
    j0=-X*Y
    j1=-X*Y**2
    j2=-(X**2)*Y
    j3=-(X**2)*Y**2
    
    J[:,0]=j0
    J[:,1]=j1
    J[:,2]=j2
    J[:,3]=j3
    
    r=Z-(P0[0]*X*Y+P0[1]*X*Y**2+P0[2]*(X**2)*Y+P0[3]*(X**2)*Y**2)
    t1=np.linalg.inv(np.dot(J.T,J))
    t2=np.dot(t1,J.T)
    t3=np.dot(t2,r)
    P1=P0-t3
    t4=abs(P1-P0)
    if max(t4)<=1e-15:
        break
    P0=P1
C0=float('{:4f}'.format(P0[0]))
C1=float('{:4f}'.format(P0[1]))
C2=float('{:4f}'.format(P0[2]))
C3=float('{:4f}'.format(P0[3]))
Zs2=(C0*Xs*Ys+C1*Xs*Ys**2+C2*(Xs**2)*Ys+C3*(Xs**2)*Ys**2)
ax.plot_surface(Xs, Ys, Zs2);
print(P0)