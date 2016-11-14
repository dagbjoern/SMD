import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con

def sigma_y(x,a_0,fa_0,a_1,fa_1,p):
    oy=np.sqrt(fa_0**2+(x*fa_1)**2+2)+2*(1*x*p*fa_0*fa_1)
    return oy

def gaus_sigma_y(x,a_0,fa_0,a_1,fa_1):
    oy=np.sqrt(fa_0**2+(x*fa_1)**2)
    return oy

def y(x,a_0,a_1):
    return a_0+a_1*x



def aufgabe_1():
    a_0=1.0  #wert von a_0
    fa_0=0.2   #fehler a_0
    a_1=1.0 #wert von a_1
    fa_1=0.2 #fehler  a_1
    p=-0.8  #Korrelationskoeffizient
    x=np.linspace(0,10)
    print('Werte von y ohne kor:',unp.uarray([y(x,a_0,a_1)],[gaus_sigma_y(x,a_0,fa_0,a_1,fa_1)]))
    print('Werte von y mit kor:',unp.uarray([y(x,a_0,a_1)],[sigma_y(x,a_0,fa_0,a_1,fa_1,p)]))


if __name__ == '__main__':
 aufgabe_1()
