import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit

#Aufgabe 3

#def aufgabe3():

def fx(x):
    f=(x**3+(1/3))-(x**3-(1/3))
    return f

def gx(x):
    g=((3+(x**3/3))-(3-(x**3/3)))/x**3
    return g



x=np.linspace(-50000,50000)


plt.figure(1)
plt.plot(x,np.abs(2/3-fx(x)),'-r',label=r'$Abweichung$')
plt.legend(loc='best')
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$\left|2/3-f(x)\right|$')
plt.ylim(0,0.01)
plt.savefig('plot 3a).pdf')



plt.figure(2)
plt.plot(x,np.abs(2/3-fx(x)),'-r',label=r'$Abweichung$')
plt.legend(loc='best')
plt.grid(True)
plt.xscale('log')
plt.ylim(0,0.01)
plt.xlabel(r'$x$')
plt.ylabel(r'$\left|2/3-f(x)\right|$')
plt.savefig('plot 3a)log.pdf')


x=np.linspace(-0.0005,0.0005)

plt.figure(3)
plt.plot(x,np.abs(2/3-gx(x)),'-r',label=r'$Abweichung$')
plt.legend(loc='best')
plt.grid(True)
plt.ylim(0,0.01)
plt.xlabel(r'$x$')
plt.ylabel(r'$\left|2/3-g(x)\right|$')
plt.savefig('plot 3b).pdf')




plt.figure(4)
plt.plot(x,np.abs(2/3-gx(x)),'-r',label=r'$Abweichung$')
plt.legend(loc='best')
plt.grid(True)
plt.xscale('log')
plt.ylim(0,0.01)
plt.xlabel(r'$x$')
plt.ylabel(r'$\left|2/3-g(x)\right|$')
plt.savefig('plot 3b)log.pdf')





#if __name__=='__main__':
#    aufgabe3()
