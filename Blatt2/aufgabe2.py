import numpy as np
from matplotlib import pyplot as plt
import numpy.random as nr


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


#rechnen

plt.plot(1)
test = gnrtr(3,100000)
plt.hist(test, bins=100)
plt.savefig("plot1.pdf")

plt.plot(2)
test = gnrtr(-2,100000)
plt.hist(test, bins=100)
plt.savefig("plot2.pdf")

plt.plot(3)
test = gnrtr(157,100000)
plt.hist(test, bins=100)
plt.savefig("plot3.pdf")

plt.plot(4)
cool = nr.randint(0,1)
plt.hist(cool,bins=100)

plt.savefig("plot4.pdf")
#ausgeben
#print(test)
