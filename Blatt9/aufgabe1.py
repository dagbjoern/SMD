import numpy as np
from scipy.optimize import fsolve
from scipy.interpolate import approximate_taylor_polynomial as taylor
from matplotlib import pyplot as plt


#groessen
#c)
lamb= 10
C   = np.log(np.math.factorial(8)) + np.log(np.math.factorial(9))+np.log(np.math.factorial(18))
C2  = 30-30*np.log(10) + C
#funktionen

def likeli(lambd):
    return(np.exp(-3*lambd) * lambd**(30) /(np.math.factorial(13)*np.math.factorial(8)*np.math.factorial(9)))


def loglikeli(lambd):
    return(3*lambd-30*np.log(lambd) + C )


def loglikeli1(lambd):
    return(3*lambd-30*np.log(lambd) + C - nlogLmax - 1/2)


def loglikeli2(lambd):
    return(3*lambd-30*np.log(lambd) + C - nlogLmax - 2)


def loglikeli3(lambd):
    return(3*lambd-30*np.log(lambd) + C - nlogLmax - 9/2)


def taylor(lambd):
    return(0.15 * lambd**2 -3 * lambd + 30/2 + C2)


def taylor1(lambd):
    return(0.15*lambd**2 -3*lambd + 30/2 +C2 - nlogLmax -1/2)


def taylor2(lambd):
    return(0.15*lambd**2 -3*lambd + 30/2 +C2 - nlogLmax - 2)


def taylor3(lambd):
    return(0.15 * lambd**2 -3 * lambd + 30 / 2 + C2 - nlogLmax - 9/2)

# rechnung
nlogLmax = loglikeli(10)

lamb1g = fsolve(loglikeli1,10.0)
lamb2g = fsolve(loglikeli2,10.0)
lamb3g = fsolve(loglikeli3,10.0)

lamb1k = fsolve(loglikeli1,1.0)
lamb2k = fsolve(loglikeli2,1.0)
lamb3k = fsolve(loglikeli3,1.0)

#d)
lambT1g = fsolve(taylor1, 10.0)
lambT2g = fsolve(taylor2, 10.0)
lambT3g = fsolve(taylor3, 10.0)

lambT1k = fsolve(taylor1, 1.0)
lambT2k = fsolve(taylor2, 1.0)
lambT3k = fsolve(taylor3, 1.0)

# Ergebnisse ausgeben
print("\nErgebnisse c): \n für +1/2: ", lamb1k,lamb1g,
"\n für +2: ", lamb2k, lamb2g,
"\n für +9/2: ", lamb3k, lamb3g)

print("\n\n Ergebnisse d): ")
print("taylor +1/2: ", lambT1g, lambT1k)
print("taylor +2: ", lambT2g, lambT2k)
print("taylor +9/2: ", lambT3g, lambT3k)


#plots
x_plot = np.linspace(0.1,20)
plt.plot(x_plot, loglikeli(x_plot), 'b',label= r'$-\ln(L(\lambda))$')
plt.xlabel(r'$\lambda$')

plt.plot(x_plot, taylor(x_plot), 'r', label= r'$T_{2}(-\ln(L(\lambda),10))$')
plt.legend(loc='best')
plt.savefig('smdblatt9plot1.pdf')
