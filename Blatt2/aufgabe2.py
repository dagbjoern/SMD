import numpy as np
from matplotlib import pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D
#import ROOT
import os
if not os.path.exists("./build"):
    os.makedirs("./build")


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

# def rootrandom(n):
#     arr = np.zeros(n)
#     rng = ROOT.TRandom()
#     for i in range(1,n):
#         arr[i] = rng.Rndm()
#     return(arr)



#plotten

#rechnen
plt.figure(1)
test1 = gnrtr(101,10000)
print('mittelwert',np.sum(test1)/10000)

plt.hist(test1, bins=40,color='b')
plt.savefig("plot1.pdf")

plt.figure(2)
test2 = gnrtr(15,10000)
print('mittelwert',np.sum(test2)/10000)
plt.hist(test2, bins=40 ,color='r')
plt.savefig("plot2.pdf")

plt.figure(3)
test3 = gnrtr(-4,10000)
print('mittelwert',np.sum(test3)/10000)

plt.hist(test3, bins=40,color='y')
plt.savefig("plot3.pdf")

plt.figure(4)
cool = nr.randint(0,1)
plt.hist(cool,bins=100)

plt.savefig("plot4.pdf")
#ausgeben
#print(test)

#e)
# plt.figure(6)
# testroot = rootrandom(10000)
# plt.hist(testroot, bins=100, color='c')
# plt.savefig("plot5.pdf")

#ausgeben
#print(test)

#print(c2D(4,10))
x,y =c2D(4,10000)
plt.figure(5)
plt.scatter(x,y)
plt.savefig('scatterplot2D.pdf')


x,y,z =c3D(4,10000)

fig = plt.figure(6)
ax = fig.add_subplot(111, projection='3d')

ax.view_init(45, 30)# Elevation , Rotation
ax.scatter(
x, y, z,
lw=0,# no lines around points
s=5,# smaller points
)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

plt.savefig('scatterplot3D.pdf')
