import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as con


#funktionen
def winkel(rho,sx,sy):
    w = 0.5 * np.arctan((2*rho*sx*sy)/(sx**2 - sy**2))
    return(w)

def laenge(alpha,sx, sy):
    l =  (1-rho**2) /(np.cos(alpha)**2 / sx**2 - 2*rho*np.sin(alpha)*np.cos(alpha) / (sx*sy) + np.sin(alpha)**2 / sy**2)
    return(l)


#werte
sx  = 3.5
sy  = 1.5
mx  = 4.0
my  = 2.0
cov = 4.2

rho        = cov/(sx*sy)
alpha      = winkel(rho,sx,sy)
hauptachsL = 2*laenge(alpha,sx, sy)
hauptachsK = laenge(alpha,sy, sx)

#ausgaben
print("korrelationkoeff.: ", rho)
print("\n winkel: ", alpha)
print("\n laenge lange hauptachse: ", hauptachsL)
print("\n laenge kurze hauptachse: ", hauptachsK)
