import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con


#Aufgabe 3

def I(p,n):
    if (p ==0 or n==0):  #wenn p oder n gleich null ist, ist die Information gleich 0
        return 0
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
    p_i=[0,0]
    n_i=[0,0]
    for i,element in enumerate(A):
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
    return Informationsgewinn(p,n,p_i,n_i)


def Informationsgewinn(p,n,p_i,n_i):
    i= I(p,n)
    E=E_a(p,n,p_i,n_i)
    return (i-E)


Temperatur=np.array([29.4,26.7,28.7,21.1,20,18.3,17.8,
            22.2,20.6,23.9,23.9,22.2,27.2,21.7])

Vorhersage=np.array([2,2,1,0,0,0,1,2,2,0,2,1,1,0])

Wind=np.array([0,1,0,0,0,1,1,0,0,0,1,1,0,1])
Luftfeuchigkeit=np.array([85,90,78,96,80,70,65,95,70,80,70,90,75,80])

Fussball=np.array([0,0,1,1,1,0,1,0,1,1,1,1,1,0])

print('Test für Wind',Schnitt(0.5,Wind,Fussball)) #test für b)



#  c)

# Schnitt für die Temperatur
x1=np.linspace(np.min(Temperatur),np.max(Temperatur),1000)
y1=np.array(x1)

for i, element in enumerate(x1):
    y1[i]=Schnitt(x1[i],Temperatur,Fussball)



plt.figure(1)
plt.plot(x1,y1,'r-',label=r'a=Temperatur')
plt.xlabel(r'Schnitt $ \ $ s')
plt.ylabel(r'gain(a)')
plt.legend(loc='best')
plt.savefig('Temperatur.pdf')

print('Temperatur max gain',np.max(y1))
print('schnitt bei' ,x1[np.argmax(y1)])


#Vorhersage
x2=np.linspace(np.min(Vorhersage),np.max(Vorhersage),1000)
y2=np.array(x2)
for i, element in enumerate(x2):
    y2[i]=Schnitt(x2[i],Vorhersage,Fussball)

plt.figure(2)
plt.plot(x2,y2,'r-',label=r'a=Vorhersage')
plt.xlabel(r'Schnitt $ \ $ s')
plt.ylabel(r'gain(a)')
plt.legend(loc='best')
plt.savefig('Vorhersage.pdf')

print('Vorhersage max gain',np.max(y2))
print('schnitt bei' ,x2[np.argmax(y2)])


#Luftfeuchigkeit
x3=np.linspace(np.min(Luftfeuchigkeit),np.max(Luftfeuchigkeit),1000)
y3=np.array(x3)
for i, element in enumerate(x3):
    y3[i]=Schnitt(x3[i],Luftfeuchigkeit,Fussball)


plt.figure(3)
plt.plot(x3,y3,'r-',label=r'a=Luftfeuchigkeit')
plt.xlabel(r'Schnitt $ \ $ s')
plt.ylabel(r'gain(a)')
plt.legend(loc='best')
plt.savefig('Luftfeuchigkeit.pdf')

print('Luftfeuchigkeit max gain',np.max(y3))
print('schnitt bei' ,x3[np.argmax(y3)])

#print(a.T)
