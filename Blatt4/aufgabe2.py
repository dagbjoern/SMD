import numpy as np
from matplotlib import pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D
import ROOT
import root_numpy
import os
if not os.path.exists("./build"):
    os.makedirs("./build")


root_file = ROOT.TFile("zwei_populationen.root", "READ")

P_0=root_file.Get("P_0_10000")
P_1=root_file.Get("P_1")


P_0 = root_numpy.root2array("zwei_populationen.root", "P_0_10000")
P_1 = root_numpy.root2array("zwei_populationen.root", "P_1")

print(P_0.dtype.names)
#
# print(P_0['x'])
# print(P_0['y'])
# print(P_0)
x=np.linspace(-15,20)
plt.figure(1)
plt.plot(P_0['x'],P_0['y'],'.m',markersize=0.75,alpha=0.3)
plt.plot(P_1['x'],P_1['y'],'.c',markersize=0.75,alpha=0.3)
plt.plot(-15,-25,'.m',alpha=0.3,label=r'P_0')
plt.plot(-15,-25,'.c',alpha=0.3,label=r'P_1')
plt.plot(x,0*x,'-r',label=r'g_1(x)')
plt.plot(x,-(3/4)*x,'-b',label=r'g_2(x)')
plt.plot(x,-(5/4)*x,'-g',label=r'g_3(x)')
plt.legend(loc='best')
plt.savefig('scatterplot2D.pdf')
a=0


#Für G_1(x)

Projektion_P_0_g1=np.zeros(P_0.shape[0])
Projektion_P_1_g1=np.zeros(P_1.shape[0])

#Projektions Vektor
g_1=np.array([-1,0])


for count, element in enumerate(P_0):
   x=np.array([element[0],element[1]])
   Projektion_P_0_g1[count]=np.dot(g_1,x)


for count, element in enumerate(P_1):
   x=np.array([element[0],element[1]])
   Projektion_P_1_g1[count]=np.dot(g_1,x)


plt.figure(2)
plt.hist(Projektion_P_0_g1,color='m',alpha=0.3,label=r'P_0')
plt.hist(Projektion_P_1_g1,color='c',alpha=0.3,label=r'P_1')
plt.legend(loc='best')
plt.savefig('g_1.pdf')


#Für G_2(x)

Projektion_P_0_g2=np.zeros(P_0.shape[0])
Projektion_P_1_g2=np.zeros(P_1.shape[0])

#Projektions Vektor
g_2=np.array([-4/5,6/10])


for count, element in enumerate(P_0):
   x=np.array([element[0],element[1]])
   Projektion_P_0_g2[count]=np.dot(g_2,x)


for count, element in enumerate(P_1):
   x=np.array([element[0],element[1]])
   Projektion_P_1_g2[count]=np.dot(g_2,x)


plt.figure(3)
plt.hist(Projektion_P_0_g2,color='m',alpha=0.3,label=r'P_0')
plt.hist(Projektion_P_1_g2,color='c',alpha=0.3,label=r'P_1')
plt.legend(loc='best')
plt.savefig('g_2.pdf')




#Für G_3(x)

Projektion_P_0_g3=np.zeros(P_0.shape[0])
Projektion_P_1_g3=np.zeros(P_1.shape[0])


#Projektions Vektor
g_3=np.array([-4/np.sqrt(41),5*np.sqrt(41)/41])
print(g_3)

for count, element in enumerate(P_0):
   x=np.array([element[0],element[1]])
   Projektion_P_0_g3[count]=np.dot(g_3,x)


for count, element in enumerate(P_1):
   x=np.array([element[0],element[1]])
   Projektion_P_1_g3[count]=np.dot(g_3,x)


plt.figure(4)
plt.hist(Projektion_P_0_g3,color='m',alpha=0.3,label=r'P_0')
plt.hist(Projektion_P_1_g3,color='c',alpha=0.3,label=r'P_1')
plt.legend(loc='best')
plt.savefig('g_3.pdf')










a=np.array([5,4])
b=np.array([[3,5],[3,5]])

print(np.dot(a,b[1]))


#c)

#Effizienz
def Effizienz(cut,signal):
    t_p=np.count_nonzero(cut<=signal)
    t_n=np.count_nonzero(cut>=signal)
    return t_p/(t_p+t_n)

def Reinheit(cut,signal,stoerung):
    t_p=np.count_nonzero(cut<=signal)
    f_p=np.count_nonzero(cut<=stoerung)
    return t_p/(f_p+t_p)


np.amax(Projektion_P_0_g1)
#c
#g_1
#
lambda_cut=np.linspace(np.amin(Projektion_P_1_g1),np.amax(Projektion_P_0_g1))
y_eff=np.array(lambda_cut)
y_rein=np.array(lambda_cut)
for i, cut in enumerate(lambda_cut):
    y_eff[i]=Effizienz(cut,Projektion_P_0_g1)
    y_rein[i]=Reinheit(cut,Projektion_P_0_g1,Projektion_P_1_g1)

plt.figure(5)
plt.plot(lambda_cut,y_eff,'r',label=r'Effizienz von g_1')
plt.plot(lambda_cut,y_rein,'b',label=r'Reinheit von g_1')
plt.legend(loc='best')
plt.xlabel(r'\lambda_cut')
plt.savefig('g_1Effizienz.pdf')

#g_2
lambda_cut=np.linspace(np.amin(Projektion_P_1_g2),np.amax(Projektion_P_0_g2))
y_eff=np.array(lambda_cut)
y_rein=np.array(lambda_cut)
for i, cut in enumerate(lambda_cut):
    y_eff[i]=Effizienz(cut,Projektion_P_0_g2)
    y_rein[i]=Reinheit(cut,Projektion_P_0_g2,Projektion_P_1_g2)

plt.figure(6)
plt.plot(lambda_cut,y_eff,'r',label=r'Effizienz von g_2')
plt.plot(lambda_cut,y_rein,'b',label=r'Reinheit von g_2')
plt.xlabel(r'\lambda_cut')
plt.legend(loc='best')
plt.savefig('g_2Effizienz.pdf')


#g_3
#
lambda_cut=np.linspace(np.amin(Projektion_P_1_g3),np.amax(Projektion_P_0_g3))
y_eff=np.array(lambda_cut)
y_rein=np.array(lambda_cut)
for i, cut in enumerate(lambda_cut):
    y_eff[i]=Effizienz(cut,Projektion_P_0_g3)
    y_rein[i]=Reinheit(cut,Projektion_P_0_g3,Projektion_P_1_g3)

plt.figure(7)
plt.plot(lambda_cut,y_eff,'r',label=r'Effizienz von g_3')
plt.plot(lambda_cut,y_rein,'b',label=r'Reinheit von g_3')
plt.legend(loc='best')
plt.xlabel(r'\lambda_cut')
plt.savefig('g_3Effizienz.pdf')
