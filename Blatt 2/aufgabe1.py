import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit
import scipy.constants as con

# Aufgabe 1
x=np.linspace(0,1000)

#a)
def fv(v,m,T):
    f=(m/(2*np.pi*con.k*T))**(3/2)*np.exp(-mv**2/(2*con.k*T))*4*np.pi*v**2
    return f




#Funktion plotten
plt.figure(1)
plt.plot(x,fx(x),'.r',label=r'$f(v)$')
plt.legend(loc='best')
plt.grid(True)
#plt.ylim(-0.5e-18,1.2e-18)
#plt.xlim(0.9985,1.0015)
plt.savefig('plot 1.pdf')
