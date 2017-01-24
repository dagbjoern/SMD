import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp



def D(N_on,N_off,alpha):
    b_0=(N_off+N_on)/(1+alpha)
    s=N_on-alpha*N_off
    b=N_off
    Lam=np.exp(N_off*np.log(b_0/b)+N_on*np.log(alpha*b_0/(s+alpha*b))-(1+alpha)*(b_0-b)+s)
    D=-np.log(Lam)
    return D




N_on_1=120
N_off_1=160
a_1=0.6

N_on_2=150
N_off_2=320
a_2=0.3


print('D1',D(N_on_1,N_off_1,a_1))

print('D2',D(N_on_2,N_off_2,a_2))
