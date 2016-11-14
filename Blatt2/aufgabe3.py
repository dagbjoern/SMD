import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con


#Aufgabe 3

def Gleichverteilung(r,x_min,x_max):
    r=np.random.rand(r)
    xr=(x_max-x_min)*r+x_min*r
    return xr

def Exponentialgesetz(r,tau):
    r=np.random.rand(r)
    xr=-tau*np.log(1-r)
    return xr

def Potenzgesetz(r,n,x_min,x_max):
    r=np.random.rand(r)
    xr=(r*(x_max**(1-n)-x_min**(1-n))+x_min**(1-n))**(1/(n-1))
    return xr

def CauchyVerteilung(r):
    r=np.random.rand(r)
    xr=np.tan((r-1/2)*np.pi)
    return xr


#data = np.load('empirisches_histogramm.npy')
#plt.hist(data['bin_mid'], bins=np.linspace(0., 1., 50),weights=data['hist'])
#plt.show()
plt.figure(1)
plt.hist(Gleichverteilung(100000,10,100),bins=100) #r=100000 x_min=10 x_max=100
plt.savefig('Gleichverteilung.pdf')

plt.figure(2)
plt.hist(Exponentialgesetz(100000,10),bins=100)  #r=100000 tau=10
plt.savefig('Exponentialgesetz.pdf')



plt.figure(3)
plt.hist(Potenzgesetz(100000,9,10,100),bins=100)  #r=100000 n=9 x_min=10 x_max=100
plt.savefig('Potenzgesetz.pdf')


plt.figure(4)
plt.hist(CauchyVerteilung(1000),bins=10000)  # r=1000
plt.axis([-100, 100, 0 ,500])
plt.savefig('CauchyVerteilung.pdf')
