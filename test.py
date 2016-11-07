import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit

gr , ge =np.genfromtxt('große_gewicht.txt',unpack=True)


plt.figure(1)
fig, ((ax11, ax21),( ax12 ,ax22) ,(ax13 ,ax23)) = plt.subplots(3, 2)

ax11.hist(gr)

ax21.hist(gr)

ax12.hist(gr)

ax22.hist(gr)

ax13.hist(gr)

ax23.hist(gr)


plt.savefig('plot größe 2a).pdf')

plt.figure(1)
fig, ((ax11, ax21),( ax12 ,ax22) ,(ax13 ,ax23)) = plt.subplots(3, 2)

ax11.hist(ge)

ax21.hist(ge)

ax12.hist(ge)

ax22.hist(ge)

ax13.hist(ge)

ax23.hist(ge)


plt.savefig('plot gewicht 2a).pdf')
