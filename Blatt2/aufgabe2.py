import numpy as np
from matplotlib import pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D

#funktionen definieren
def gnrtr(xs, n):
    a = 1601
    b = 3456
    m = 10000

    arr = np.zeros(n)
    arr[0] = np.mod((a*xs + b),m)
    for i in range(1,n):
            arr[i] = np.mod((a*arr[i-1] + b),m)
    return(arr/m)


def c2D(xs, n):
    a = 1601
    b = 3456
    m = 10000

    arr = np.array([np.zeros(n),np.zeros(n)])
    arr[0,0] = np.mod((a*xs + b),m)
    for i in range(1,n):
            arr[0,i] = np.mod((a*arr[0,i-1] + b),m)
            arr[1,i-1]=np.mod((a*arr[0,i-1] + b),m)
    arr[1,i]=np.mod((a*arr[0,i] + b),m)
    return(arr/m)


def c3D(xs, n):
    a = 1601
    b = 3456
    m = 10000

    arr = np.array([np.zeros(n),np.zeros(n),np.zeros(n)])
    arr[0,0] = np.mod((a*xs + b),m)
    for i in range(1,n):
            arr[0,i] = np.mod((a*arr[0,i-1] + b),m)
            arr[1,i-1]=np.mod((a*arr[0,i-1] + b),m)
            arr[2,i-1]=np.mod((a*arr[1,i-1] + b),m)
    arr[1,i]=np.mod((a*arr[0,i] + b),m)
    arr[2,i]=np.mod((a*arr[1,i] + b),m)
    return(arr/m)





#rechnen
plt.figure(1)
test = gnrtr(101,10000)
print('mittelwert',np.sum(test)/10000)

plt.hist(test, bins=100,color='b')
plt.savefig("plot1.pdf")

plt.figure(2)
test = gnrtr(100,10000)
print('mittelwert',np.sum(test)/10000)
plt.hist(test, bins=100 ,color='r')
plt.savefig("plot2.pdf")

plt.figure(3)
test = gnrtr(157,10000)
print('mittelwert',np.sum(test)/10000)

plt.hist(test, bins=100,color='y')
plt.savefig("plot3.pdf")

plt.figure(4)
cool = nr.randint(0,1)
plt.hist(cool,bins=100)

plt.savefig("plot4.pdf")
#ausgeben
#print(test)

#print(c2D(4,10))
x,y =c2D(4,10000)
plt.figure(5)
plt.scatter(x,y)
plt.savefig('scatterplot2D.pdf')


x,y,z =c3D(4,10000)

print(x)
print(y)
print(z)

fig = plt.figure(6)
ax = fig.add_subplot(111, projection='3d')
n = 100

ax.scatter(x, y, z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig('scatterplot3D.pdf')
