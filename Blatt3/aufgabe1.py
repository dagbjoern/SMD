import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con
import ROOT
import root_numpy

#groessen
phik  = 1
gamma = 2.7
Emin  = 1 # in Tev

#funktionen
def phi(E):
    return(phik * Emin**(-gamma))

def P(E):
    return((1 - np.e**(-E/2))**3)

def E(r):
    return((1/(1-r))**(1/(gamma -1)))

def polar(r):
    return(1 - np.e**(-r**2 /2))

def sigma(N):
    return(1/(np.log10(N + 1)))

def normal():#erzeuge normalverteilte x1, x2
    s = 2
    v1 = 0
    v2 = 0
    while (s>1):
        v1 = 2*np.random.rand(1) -1
        v2 = 2*np.random.rand(1) -1
        s  = v1**2 + v2**2
    r      = np.sqrt(s)
    theta  = np.arctan(v2/v1)
    v1     = r*np.cos(theta)
    v2     = r*np.cos(theta)
    x1     = v1*np.sqrt(-2*np.log(s) /s)
    x2     = v2*np.sqrt(-2*np.log(s) /s)
    return (np.array((x1,x2)))

#a) simulation neutrino Fluss
zahlen = np.random.rand(10**5)#zufallszahlen
Esim   = E(zahlen)#simulierte eien
phisim = phi(Esim)#wird gar nicht gebraucht
space  = np.linspace(1,10,50)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1,10)
plt.hist(Esim,bins=space, color ='r',  label=r'$\mathrm{Simulierte \ Signale}$')

#in root tree speichern
rec = np.array(Esim, dtype=[("eie", np.float)])
root_numpy.array2root(rec, "NeturinoMC.root", treename = "Signal_MC", mode = "RECREATE")

#b)
zahlen2 = np.random.rand(10**5)#nochmal zufallszahlen
aktzeptw = P(Esim)

akzeptE = Esim[zahlen2 < aktzeptw]#prüfe aktzeptanz
plt.hist(akzeptE, bins=space, color='b', label=r'$\mathrm{Aktzeptierte \ Signale}$')
plt.legend(loc='best')
plt.savefig('plotsAB.pdf')

#in root tree speichern
rec2 = np.array(akzeptE, dtype=[("eie", np.float)])
root_numpy.array2root(rec2, "NeturinoMC.root", treename = "Signal_MC_Akzeptanz", mode = "RECREATE")


#c)
#polarverfahren
hits = np.zeros(len(akzeptE))
for i, energ in enumerate(akzeptE):
    while 1==1:
        x,y = normal()*energ*2 + energ*10
        if x>0 or y>0:
            break
    if x >0:
        hits[i] = np.round(x)#hits nur ganzzahlig
    else:
        hits[i] = np.round(y)

#d) läuft mit dem folgenden teil nicht durh
#positionen
#loc = np.zeros((len(hits), 2))
#for i, h in enumerate(hits):#koordinaten produzieren
#    while 1==1 :
#        o1 = np.random.normal( loc = 7, scale = 1/(np.log10(h + 1)))
#        o2 = np.random.normal( loc = 3, scale = 1/(np.log10(h + 1)))
#    if o1 >0 and o1 <10 and o2 >0 and o2 >10:
#        break

    #zulässige koordinaten als orte speichern
#    loc[i] = (o1,o2)

# Leider Zeitprobleme
