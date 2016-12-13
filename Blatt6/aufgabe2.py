import numpy as np
from matplotlib import pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D
import ROOT
import root_numpy



def C(f):
    1/m  
    return






root_file = ROOT.TFile("zwei_populationen.root", "READ")

P_0=root_file.Get("P_0_10000")
P_1=root_file.Get("P_1")


P_0 = root_numpy.root2array("zwei_populationen.root", "P_0_10000")
P_1 = root_numpy.root2array("zwei_populationen.root", "P_1")

print(P_0.dtype.names)
