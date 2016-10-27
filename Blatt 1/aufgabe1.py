import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit

# Aufgabe 1
def aufgabe1():
    x=np.linspace(0.999,1.001,1000)

    #a)

    def fx(x):
        f=(1-x)**6 #funktion für a
        return f




#Funktion plotten
    plt.figure(1)
    plt.plot(x,fx(x),'.r',label=r'$f(x)=(1-x)^6$')
    plt.legend(loc='best')
    plt.grid(True)
    plt.ylim(-0.5e-18,1.2e-18)
    plt.xlim(0.9985,1.0015)
    plt.savefig('plot 1a).pdf')

#b)

    def fxb(x):
        f=x**6-6*x**5+15*x**4-20*x**3+15*x**2-6*x+1 #funktion für b
        return f

#Funktion plotten
    plt.figure(2)
    plt.plot(x,fxb(x),'.r',label=r'$f(x)=x^6-6x^5+15x^4-20x^3+15x^2-6x+1$')
    plt.legend(loc='best')
    plt.grid(True)
    plt.xlim(0.9985,1.0015)
    plt.savefig('plot 1b).pdf')


    def  fxc(x):
        f=(((((x-6)*x+15)*x-20)*x+15)*x-6)*x+1 #funktion für c
        return f


        #Funktion plotten
        plt.figure(3)
        plt.plot(x,fxc(x),'.r',label=r'$f(x)=(((((x-6)x+15)x-20)x+15)x-6)x+1$')
        plt.legend(loc='best')
        plt.grid(True)
        plt.xlim(0.9985,1.0015)
        plt.savefig('plot 1c).pdf')

if __name__=='__main__':
    aufgabe1()
