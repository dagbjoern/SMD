import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as con


#funktionen
def d1(th):
    return ((con.alpha**2 /s * ((2 + np.sin(th)**2)/(1- beta**2 * np.cos(th)**2))))

def d2(th):
    return((con.alpha**2 /s * ((2 + np.sin(th)**2)/(np.sin(th)**2 + gamma**(-2) * np.cos(th)**2))))




def k(th):
    ze = (1-3*beta**2) * th * np.sin(2*th) * (1 - beta**2 * np.cos(th)**2)
    n  = (np.sin(th)**2 + 2) * (beta**2 * np.cos(th)**2 - 1)**2
    return(abs(ze/n))

#groessen
E     = 50 * 10**(9) * con.elementary_charge
gamma = (50 * 10**9)/(511 * 10**3)
beta  = np.sqrt(1 - gamma**(-2))
s     = (E*2)**2

#plotten
# grenze
g = 10**(-7)
th_plot = np.linspace(np.pi -g,np.pi + g,2000)


plt.figure(1)
plt.xlim(np.pi - g,np.pi + g)
plt.plot(th_plot, d1(th_plot), 'r', label=r'$\mathrm{Plot \ instabil}$')
plt.plot(th_plot, d2(th_plot), 'g', label=r'$\mathrm{Plot \ stabil}$')




plt.xlabel(r'$\theta$')
plt.ylabel(r'f(\theta)$')
plt.legend(loc='best')
plt.savefig('plot 4c).pdf')

#plotten part2
plt.figure(2)
th_space = np.linspace(0, np.pi, 1000)
plt.xlim(0, np.pi)
plt.plot(th_space, k(th_space), 'b', label=r'$\mathrm{Konditionszahl \ K}$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$K(\theta)$')
plt.legend(loc='best')
plt.savefig('plot 4e).pdf')
