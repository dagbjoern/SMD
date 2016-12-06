import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con
import ROOT
import root_numpy


root_file = ROOT.TFile("zwei_populationen.root", "READ")

P_0=root_file.Get("P_0_10000")
P_1=root_file.Get("P_1")


P_0 = root_numpy.root2array("zwei_populationen.root", "P_0_10000")
P_1 = root_numpy.root2array("zwei_populationen.root", "P_1")


#a) Mittelwerte



mu_P0=np.array([np.mean(P_0['x']),np.mean(P_0['y'])])
mu_P1=np.array([np.mean(P_1['x']),np.mean(P_1['y'])])

print('mu_P0',mu_P0)
print('mu_P1',mu_P1)
#   Kovantianzmatrix
P0 = np.array([P_0['x'],P_0['y']])
P1 = np.array([P_1['x'],P_1['y']])
P0=P0.T
P1=P1.T
#   S_P0
for index,element in enumerate(P0):
    if index==0:
        S_P0=np.outer(element-mu_P0,element-mu_P0)
    S_P0=S_P0+np.outer(element-mu_P0,element-mu_P0)

print('S_P0',S_P0)

#   S_P1
for index,element in enumerate(P1):
    if index==0:
        S_P1=np.outer(element-mu_P1,element-mu_P1)
    S_P1=S_P1+np.outer(element-mu_P1,element-mu_P1)

print('S_P1',S_P1)

#   S_P0P1
S_P0P1=S_P0+S_P1
print('S_P0P1=',S_P0P1)
#S_B
S_B=np.outer(mu_P0-mu_P1,mu_P0-mu_P1)
print('S_B=',S_B)


inv_S_P0P1=np.linalg.inv(S_P0P1)
print('inverse',inv_S_P0P1)
#Matrix für das eigenwertproblem A=S_W^(-1)S_B
A=np.dot(inv_S_P0P1,S_B)
print('A',A)
w , v =np.linalg.eig(A)  # w= Eigenwerte , v= Eigenvektoren
print('Eigenwerte',w)
print('Eigenvektoren',v)
v=v.T
print('probe w=1:',np.dot(A-np.diag([w[1],w[1]]),v[1]))

print('probe.',np.dot(v[0],v[1]))
print('länge v',np.sqrt(v[1][0]**2+v[1][1]**2))


#lambda'
#v_test=np.dot(inv_S_P0P1,mu_P0-mu_P1)
#print(v_test,v[1])

#  c)
# Geradengleichung

lambda_1=w[0]*v[0]
#geradensteigung
m=lambda_1[1]/lambda_1[0]
print('steigung der Geraden m',m)
print(lambda_1)


#d)
Projektion_P_0=np.zeros(P_0.shape[0])
Projektion_P_1=np.zeros(P_1.shape[0])

for count, element in enumerate(P_0):
   x=np.array([element[0],element[1]])
   Projektion_P_0[count]=np.dot(-v[0],x)


for count, element in enumerate(P_1):
   x=np.array([element[0],element[1]])
   Projektion_P_1[count]=np.dot(-v[0],x)


plt.figure(10)
plt.hist(Projektion_P_0,color='m',alpha=0.3,label=r'$P0$')
plt.hist(Projektion_P_1,color='c',alpha=0.3,label=r'$P1$')
plt.legend(loc='best')
plt.savefig('Projektion.pdf')



#   e)
#Effizienz
def Effizienz(cut,signal):
    t_p=np.count_nonzero(cut<=signal)
    f_n=np.count_nonzero(cut>=signal)
    return t_p/(t_p+f_n)

def Reinheit(cut,signal,stoerung):
    t_p=np.count_nonzero(cut<=signal)
    f_p=np.count_nonzero(cut<=stoerung)
    return t_p/(t_p+f_p)

def Signal_zu_Untergrund(cut,signal,stoerung):
    t_p=np.count_nonzero(cut<=signal)
#    print('t_p',t_p)
    f_p=np.count_nonzero(cut<=stoerung)
#    print('f_p',f_p)
    t_n=np.count_nonzero(cut>=stoerung)
#    print('t_n',t_n)
    f_n=np.count_nonzero(cut>=signal)
#    print('f_n',f_n)
    return(t_p/f_p)

def Signifikanz(cut,signal,stoerung):
    t_p=np.count_nonzero(cut<=signal)
    f_p=np.count_nonzero(cut<=stoerung)
    return(t_p/np.sqrt(t_p+f_p))

lambda_cut=np.linspace(np.amin(Projektion_P_1),np.amax(Projektion_P_0))
y_eff=np.array(lambda_cut)
y_rein=np.array(lambda_cut)
y_verhaeltnis=np.array(lambda_cut)
y_sig=np.array(lambda_cut)

for i, cut in enumerate(lambda_cut):
    y_eff[i]=Effizienz(cut,Projektion_P_0)
    y_rein[i]=Reinheit(cut,Projektion_P_0,Projektion_P_1)
    y_sig[i]=Signifikanz(cut,Projektion_P_0,Projektion_P_1)

print('Maximum Signifikanz',lambda_cut[np.where(y_sig==np.amax(y_sig))])


plt.figure(2)
plt.plot(lambda_cut,y_eff,'r',label=r'Effizienz von $\lambda_{cut}$')
plt.plot(lambda_cut,y_rein,'b',label=r'Reinheit von $\lambda_{cut}$')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('Eff_Rein.pdf')


plt.figure(4)
plt.plot(lambda_cut,y_sig,'r',label=r'Signifikanz')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('Signifikanz.pdf')

lambda_cut=np.linspace(np.amin(Projektion_P_1),np.amax(Projektion_P_1))
for i, cut in enumerate(lambda_cut):
    y_verhaeltnis[i]=Signal_zu_Untergrund(cut,Projektion_P_0,Projektion_P_1)

print('Maximum verhältis S/B',lambda_cut[np.where(y_verhaeltnis==np.amax(y_verhaeltnis))])

plt.figure(3)
plt.plot(lambda_cut,y_verhaeltnis,'m',label=r'Signal-zu-Untergrundverhältnis S/B')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('verhaeltnis.pdf')






# h)



P_0 = root_numpy.root2array("zwei_populationen.root", "P_0_1000")

Projektion_P_0=np.zeros(P_0.shape[0])

for count, element in enumerate(P_0):
   x=np.array([element[0],element[1]])
   Projektion_P_0[count]=np.dot(-v[0],x)


plt.figure(11)
plt.hist(Projektion_P_0,color='m',alpha=0.3,label=r'$P0$')
plt.hist(Projektion_P_1,color='c',alpha=0.3,label=r'$P1$')
plt.legend(loc='best')
plt.savefig('Projektion_h).pdf')



lambda_cut=np.linspace(np.amin(Projektion_P_1),np.amax(Projektion_P_0))
y_eff=np.array(lambda_cut)
y_rein=np.array(lambda_cut)
y_sig=np.array(lambda_cut)
for i, cut in enumerate(lambda_cut):
    y_eff[i]=Effizienz(cut,Projektion_P_0)
    y_rein[i]=Reinheit(cut,Projektion_P_0,Projektion_P_1)
    y_sig[i]=Signifikanz(cut,Projektion_P_0,Projektion_P_1)

print('Maximum Signifikanz',lambda_cut[np.where(y_sig==np.amax(y_sig))])

plt.figure(5)
plt.plot(lambda_cut,y_eff,'r',label=r'Effizienz von $\lambda_{cut}$')
plt.plot(lambda_cut,y_rein,'b',label=r'Reinheit von $\lambda_{cut}$')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('Eff_Rein_h).pdf')

plt.figure(7)
plt.plot(lambda_cut,y_sig,'r',label=r'Signifikanz')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('Signifikanz_h).pdf')


lambda_cut=np.linspace(np.amin(Projektion_P_1),np.amax(Projektion_P_1))

for i, cut in enumerate(lambda_cut):
    y_verhaeltnis[i]=Signal_zu_Untergrund(cut,Projektion_P_0,Projektion_P_1)

print('Maximum verhältis S/B',lambda_cut[np.where(y_verhaeltnis==np.amax(y_verhaeltnis))])

plt.figure(8)
plt.plot(lambda_cut,y_verhaeltnis,'m',label=r'Signal-zu-Untergrundverhältnis S/B')
plt.xlabel(r'$\lambda_\mathrm{cut}$')
plt.legend(loc='best')
plt.savefig('verhaeltnis_h).pdf')
