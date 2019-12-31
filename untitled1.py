# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:57:47 2019

@author: Administrator
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Administrator\\Desktop\\Salary_Data.csv")

char=df.columns
x=df[char[0]]
y=df[char[1]]
count=len(x)
plt.scatter(x,y)

'''
class Lineral_Regression():
    def __init__(self,regularized=True,learning_rate=0.002,momentum=0.9,datasets):
#最小二乘:
a=(np.sum(x*y) - count*np.mean(x)*np.mean(y))/(np.sum(x**2)-count*(np.mean(x)**2))
b=np.mean(y)-a*np.mean(x)
figure=plt.figure()
plt.plot(x,a*x+b)
val=float(input("input how long you have work"))
print("your salary is %f"%(a*val+b))
'''
def mse_gradient(x_data,y_data,cov,shift,regularized=True):
    if regularized:
         return -2*np.sum(x_data*(y_data-cov*x_data-shift))/count+a,-2*np.sum(y_data-cov*x_data-shift)
    else:
         return -2*np.sum(x_data*(y_data-cov*x_data-shift))/count,-2*np.sum(y_data-cov*x_data-shift)
#梯度下降：带动量的SGD
lr=0.002
momentum=0.9
v,u=0,0
a=100
b=100
for iters in range(1000):
    parameter=mse_gradient(x,y,a,b,True)#true带正则 false不带正则
    v=momentum*v-lr*parameter[0]
    u=momentum*u-lr*parameter[1]
    a=a+v
    b=b+u
plt.plot(x,a*x+b)
val=float(input("input how long you have worked"))
print("your salary is %f"%(a*val+b))