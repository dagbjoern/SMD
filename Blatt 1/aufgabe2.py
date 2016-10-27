import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit


#Aufgabe 2
def aufgabe2():

#b

#Definition der Funktion
    def fx(x):
        f=(np.sqrt(9-x)-3)/x
        return f

        x=np.logspace(-1,-20,20)#Anlegen des Werte Bereiches

        plt.figure(1)
        plt.plot(x,fx(x),'.r',label=r'$f(x)=\frac{\sqrt{9-x}-3}{x}$')
        plt.legend(loc='best')
        plt.grid(True)
        plt.xscale('log')
        plt.ylim(-0.25,0.05)
        #plt.xlim(0.9985,1.0015)
        plt.savefig('plot 2b).pdf')


if __name__=='__main__':
    aufgabe2()
