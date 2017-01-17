import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import pandas as pd

x=np.linspace(0,330,12)
x=x*np.pi/180
a=np.cos(x)

b=np.sin(x)

A=np.array([a,b]).T
y=np.array([-0.032,0.010,0.057,0.068,0.076,0.080,0.031,0.005,-0.041,-0.090,-0.088,-0.074])

cool=np.dot(A.T,y)
a=np.dot(np.array([ [1/6,0],[0,1/6] ]),cool)
print(a)

ATA=np.array([[6,0],[0,6]])

ATA_1=np.array([ [1/6,0],[0,1/6] ])
print(ATA)

S=np.dot(y.T,y)-np.dot(a.T,np.dot(A.T,y))

n=12
p=2
sigma_2=S/(-p)

print(sigma_2)

Va=sigma_2*ATA_1

print(Va)
