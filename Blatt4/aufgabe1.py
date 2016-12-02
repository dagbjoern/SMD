import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import scipy.constants as con


mu_x_0=0
mu_y_0=3
sigma_x_0=3.5
sigma_y_0=2.6
rho_0=0.9
mean_0=np.array([mu_x_0,mu_y_0])
cov_0 =[[sigma_x_0**2,rho_0*sigma_x_0*sigma_y_0],[rho_0*sigma_x_0*sigma_y_0,sigma_y_0**2]]


mu_x_1=6
a=-0.5
b=0.6
# linearität des Erwartungswertes
mu_y_1=a+b*mu_x_1
sigma_x_1=3.5
x=np.random.normal(mu_x_1,sigma_x_1,1000)
y=a+b*x


def korrelation(x_mean,y_mean,y,x):
    S_xy=0
    S_xx=0
    S_yy=0
    for i,element in enumerate(x):
            S_xy=S_xy+(x[i]-x_mean)*(y[i]-y_mean)
            S_xx=S_xx+(x[i]-x_mean)**2
            S_yy=S_yy+(y[i]-y_mean)**2
    return S_xy/(S_xx*S_yy)**(0.5)

rho_1=korrelation(mu_x_1,mu_y_1,x,y)

print(rho_1)
sigma_y_1=1
mean_1=np.array([mu_x_1,mu_y_1])
cov_1 =[[sigma_x_1**2,rho_1*sigma_x_1*sigma_y_1],[rho_1*sigma_x_1*sigma_y_1,sigma_y_1**2]]


x0, y0=np.random.multivariate_normal(mean_0,cov_0 ,10000).T
x1, y1=np.random.multivariate_normal(mean_1,cov_1 ,10000).T

plt.figure(1)
plt.plot(x0,y0,'.m',markersize=0.75,alpha=0.3)
plt.plot(x1,y1,'.c',markersize=0.75,alpha=0.3)
#plt.legend(loc='best')
plt.savefig('scatterplot2Da.pdf')
