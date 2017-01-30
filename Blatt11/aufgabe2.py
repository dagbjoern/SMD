import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp



def chi_2(y,fx,sigma):
    return np.sum(((y-fx)**2)/((sigma)**2))


y=np.array([31.6,32.2,31.2,31.9,31.3,30.8,31.3])

#Hypothese
A=31.3
sigma=0.5
B=30.7
n=7 #freiheitsgerade

print('a) x^2=',chi_2(y,A,sigma))
print(chi_2(y,A,sigma)/n)
print('b) x^2=',chi_2(y,B,sigma))
print(chi_2(y,B,sigma)/n)
