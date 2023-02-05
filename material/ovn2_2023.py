# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np

x=np.array([[1,2,3,4]])
A=np.array([[1,2],[3,4],[5,6],[7,8]])
b=np.array([[1,1]])

def test(x,A,b):
    C=np.matmul(x,A)+b
    return C

utdata=test(x,A,b)

