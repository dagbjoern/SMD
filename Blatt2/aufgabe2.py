import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit


#Aufgabe 2


#a

gr , ge =np.genfromtxt('große_gewicht.txt',unpack=True)


plt.figure(1)
fig, ((ax11, ax21),( ax12 ,ax22) ,(ax13 ,ax23)) = plt.subplots(3, 2)

ax11.hist(gr,bins=5)
ax11.set_title('Bins=5')

ax21.hist(gr,bins=10)
ax21.set_title('Bins=10')

ax12.hist(gr,bins=15)
ax12.set_title('Bins=15')

ax22.hist(gr,bins=20)
ax22.set_title('Bins=20')

ax13.hist(gr,bins=30)
ax13.set_title('Bins=30')

ax23.hist(gr,bins=50)
ax23.set_title('Bins=50')


fig.tight_layout()
plt.savefig('plotgr2a).pdf')

plt.figure(2)
fig, ((ax11, ax21),( ax12 ,ax22) ,(ax13 ,ax23)) = plt.subplots(3, 2)

ax11.hist(ge,bins=5)
ax11.set_title('Bins=5')

ax21.hist(ge,bins=10)
ax21.set_title('Bins=10')

ax12.hist(ge,bins=15)
ax12.set_title('Bins=15')

ax22.hist(ge,bins=20)
ax22.set_title('Bins=20')

ax13.hist(ge,bins=30)
ax13.set_title('Bins=30')

ax23.hist(ge,bins=50)
ax23.set_title('Bins=50')


fig.tight_layout()
plt.savefig('plotge2a).pdf')


x = np.random.randint(1,100,10**5)
x= np.log(x)
plt.figure(3)
fig, ((ax11, ax21),( ax12 ,ax22) ,(ax13 ,ax23)) = plt.subplots(3, 2)

ax11.hist(x,bins=5)
ax11.set_title('Bins=5')


ax21.hist(x,bins=10)
ax21.set_title('Bins=10')



ax12.hist(x,bins=15)
ax12.set_title('Bins=15')

ax22.hist(x,bins=20)
ax22.set_title('Bins=20')

ax13.hist(x,bins=30)
ax13.set_title('Bins=30')

ax23.hist(x,bins=50)
ax23.set_title('Bins=50')


fig.tight_layout()
plt.savefig('plot2c).pdf')
