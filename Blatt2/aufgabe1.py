import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit
import scipy.constants as con
import scipy.integrate as integrate
import scipy.special as special


# Aufgabe 1
#c)

def f(v,v_m):
    f=(1/(4*np.pi*(v_m**2)))**(2/3)*np.exp(-(v**2/(4*np.pi*v_m**2)))*4*np.pi*v^2
  return f

v_median=x*v_m

  result = integrate.quad(lambda v: f(v,), 0, v_median)
  if result==0.5
