import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con


#Aufgabe 3

def I(p,n):
    # print(p,n)
    x=-(p/(p+n))*np.log2(p/(p+n))-(n/(p+n))*np.log2(n/(p+n))
    return x


def E_a(p,n,p_i,n_i):
    E_A=0
    for index,element in enumerate(p_i):
            E_A=E_A+((element+n_i[index])/(p+n))*I(element,n_i[index])
    return E_A

def Schnitt(s,A,Fuss):
    Matrix=np.array([A,Fuss])
    T=Matrix.T
    p=np.count_nonzero(T.T[1])
    n=len(Fuss)-p
    # print(n,p)
    p_i=[0,0]
    n_i=[0,0]
    for i,element in enumerate(A):
    #    print(element)
        if (element>=s):
            if (T[i][1]==1):
                p_i[0]=p_i[0]+1
            if (T[i][1]==0):
                n_i[0]=n_i[0]+1
        if (element<s):
            if (T[i][1]==1):
                p_i[1]=p_i[1]+1
            if (T[i][1]==0):
                n_i[1]=n_i[1]+1
        #print(p_i,n_i)
    return Informationsgewinn(p,n,p_i,n_i)


def Informationsgewinn(p,n,p_i,n_i):
    i= I(p,n)
    E=E_a(p,n,p_i,n_i)
#    print(i-E)
    return (i-E)


Temperatur=np.array([29.4,26.7,28.7,21.1,20,18.3,17.8,
            22.2,20.6,23.9,23.9,22.2,27.2,21.7])

Wetter=np.array([2,2,1,0,0,0,1,2,2,0,2,1,1,0])

Wind=np.array([0,1,0,0,0,1,1,0,0,0,1,1,0,1])
Luftfeuchigkeit=np.array([85,90,78,96,80,70,65,95,70,80,70,90,75,80])

Fussball=np.array([0,0,1,1,1,0,1,0,1,1,1,1,1,0])

print(Schnitt(0.5,Wind,Fussball)) #test für b)



#  c)
# Schnitt für die Temperatur

x=np.linspace(1+np.min(Temperatur),np.max(Temperatur)-1)
y=np.array(x)

for i, element in enumerate(x):
    y[i]=Schnitt(x[i],Temperatur,Fussball)



plt.figure(1)
plt.plot(x,y,'r-',)
plt.savefig('Temperatur.pdf')



#wetter
x=np.linspace(0.1,1.9)
y=np.array(x)
for i, element in enumerate(x):
    y[i]=Schnitt(x[i],Wetter,Fussball)

plt.figure(2)
plt.plot(x,y,'r-',)
plt.savefig('Wetter.pdf')

#Luftfeuchigkeit
x=np.linspace(np.min(Luftfeuchigkeit)+1,np.max(Luftfeuchigkeit))
y=np.array(x)
for i, element in enumerate(x):
    y[i]=Schnitt(x[i],Luftfeuchigkeit,Fussball)


plt.figure(3)
plt.plot(x,y,'r-',)
plt.savefig('Luftfeuchigkeit.pdf')
