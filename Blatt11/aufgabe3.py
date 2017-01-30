import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import pandas as pd

def potenz(x,i):
    return(x**i)

def polynom(x,para):
    f=0
    for i,value in enumerate(para):
        f=f+value*x**i
    return f
#a)
x,y =np.genfromtxt('aufg_a.txt',unpack=True)


A=np.zeros((8,7))


                        #erstellen der Design-Matrix
for index,value in enumerate(x):
     for i in range(0,7):
          A[index,i]=potenz(value,i)

x_fit=np.linspace(0,8,10000)
inverse=np.linalg.inv(np.dot(A.T,A))

a=np.dot(inverse,np.dot(A.T,y))
print('a_a=',a)
plt.figure(1)
plt.plot(x,y,'xk',label=r'Datenpunkte')
plt.plot(x_fit,polynom(x_fit,a),'-b',label=r'Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.savefig('Fit.pdf')

#b)
def C(size):
    c=np.zeros([size,size])
    for i in range(1,(size)):# np.linspace(1,size-2,size-2)):
        c[(i,i)]=-2
        c[(i-1,i)]=1
        c[(i,i-1)]=1
    c[(0,0)]=-1
    c[(size-1,size-1)]=-1
    return c

def regfit(A,lam,y):
    gamma=np.sqrt(lam)*np.dot(C(len(A)),A)
    a=np.dot(np.linalg.inv(np.dot(A.T,A)+np.dot(gamma.T,gamma)),np.dot(A.T,y))
    return a

lam=np.array([0.1,0.3,0.7,3,10])


a_reg=np.array([
regfit(A,lam[0],y),
regfit(A,lam[1],y),
regfit(A,lam[2],y),
regfit(A,lam[3],y),
regfit(A,lam[4],y)
])

#np.savetxt('a_reg.txt',a_reg)

print('a(0,3)=',regfit(A,lam[1],y))

plt.figure(2)
plt.plot(x,y,'xk',label=r'Datenpunkte')
plt.plot(x_fit,polynom(x_fit,regfit(A,lam[0],y)),'--b',label=r'Fit $\lambda=0.1$')
plt.plot(x_fit,polynom(x_fit,regfit(A,lam[1],y)),'--c',label=r'Fit $\lambda=0.3$')
plt.plot(x_fit,polynom(x_fit,regfit(A,lam[2],y)),'--m',label=r'Fit $\lambda=0.7$')
plt.plot(x_fit,polynom(x_fit,regfit(A,lam[3],y)),'--y',label=r'Fit $\lambda=3$')
plt.plot(x_fit,polynom(x_fit,regfit(A,lam[4],y)),'--g',label=r'Fit $\lambda=10$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.savefig('Fit_b).pdf')


#c
M =np.genfromtxt('aufg_c.csv',delimiter=',')

x_c=M.T[0]
y_c=M.T[1:51]

def fehler(x,mean_x):
    n=len(x)
    return np.sqrt((1/(n-1))*np.sum((x-mean_x)**2))





for i in range(0,8):
    if i==0:
        mittelwerte=np.array([np.mean(y_c.T[i])])
        fehler_mittelwerte=np.array([fehler(y_c.T[i],np.mean(y_c.T[i]))])
    else:
        mittelwerte=np.append([mittelwerte],[np.mean(y_c.T[i])])
        fehler_mittelwerte=np.append([fehler_mittelwerte],[fehler(y_c.T[i],np.mean(y_c.T[i]))])

print('mittelwerte',mittelwerte)
print('feher_mittelwerte',fehler_mittelwerte)

w=np.diag(1/(fehler_mittelwerte**2))

def gewFit(A,W,y):
    AWA=np.dot(A.T,np.dot(W,A))
    AWy=np.dot(A.T,np.dot(W,y))
    return np.dot(np.linalg.inv(AWA),AWy)

print('gew a',gewFit(A,w,mittelwerte))
plt.figure(3)
for index, value in enumerate(mittelwerte):
    plt.errorbar(x[index],value,yerr=fehler_mittelwerte[index],fmt='xr')
plt.plot(x_fit,polynom(x_fit,gewFit(A,w,mittelwerte)),'--b',label=r'Fit $\lambda=0.1$')
plt.plot(x,mittelwerte,'xk',label=r'Mittelwerte')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.savefig('Fit_c).pdf')
