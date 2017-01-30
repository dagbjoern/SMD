import numpy as np
import ROOT
import root_numpy

#funktionen

def euklid(vec):#bestimmt längen der Abstandsvektoren euklidisch
    wert = 0.0
    for i in range(0,len(vec)):
        wert += vec[i]**2
    return(np.sqrt(wert))


def neighbors(sample, label, dat, k):#findet die k naechsten nachbarn
    dist = np.zeros(len(sample))#array fuer abstaende
    for j in range(0,len(sample)):
        dist[j] = euklid(sample[j] - dat)#abstaende bestimmen und speichern
    sort = np.argsort(dist)#sortiere abstaende
    nlabel = np.empty(k,dtype=object)
    for l in range(0,k):
        nlabel[l]    = label[sort[l]]#waehlt die labels der k naechsten nachbarn aus
    sortnlabel = np.sort(nlabel)#sortiert die labels alphabetisch
    leader = sortnlabel[0]#immer das aktuell haeufigste label
    potleader = sortnlabel[0]#potentiell naechstes haeufigstes label (erhaeltl diesen wert nur zur initialisieren)
    potleadcount = 0
    leadcount = 0
    count = 0
    while(count <k):          #nun wird das array mit den labels durchlaufen und jeweils das haeufigste label aktualisiert
        while(sortnlabel[count] == leader):
            if (count >= k-2):
                break
            leadcount +=1
            count     +=1

        if (count >= k-1):
            break
        potleader = sortnlabel[count]
        potleadcount = 0
        while(sortnlabel[count] == potleader):
            potleadcount +=1
            count        +=1
            if (count >= k):
                break

        if (potleadcount > leadcount):
            leader = potleader
            leadcount = potleadcount
        if (count>= k-1):
            break
    return(leader)

def knnanwendung(sample, label, data, k):
    result = np.empty(len(data), dtype=object)
    for s in range(0,len(data)):#laeuft alle testdaten durch
        result[s] = neighbors(sample, label, data[s], k)#bewertet einzeln jeden Testdatenpunkt
    anzahlsig = len(result[result == 's'])#zaehlt anzahl der als signal klassifizierten events
    anzahlbac = len(result[result == 'u'])
    return(anzahlsig, anzahlbac, result)



#root file entpacken

root_file = ROOT.TFile("NeutrinoMC.root", "READ")
#anzeigen
for key in root_file.GetListOfKeys():
    print(key.GetName())

tree1 = root_file.Get("Signal_MC")
branches = tree1.GetListOfBranches()
for branch in branches:
    print(branch.GetName())
print("\n")
tree2 = root_file.Get("Signal_MC_Akzeptanz")
branches = tree2.GetListOfBranches()
for branch in branches:
    print(branch.GetName())
print("\n")
tree3 = root_file.Get("Untergrund_MC")
branches = tree3.GetListOfBranches()
for branch in branches:
    print(branch.GetName())

#einlesen
sig = root_numpy.root2array("NeutrinoMC.root", "Signal_MC_Akzeptanz")
bac = root_numpy.root2array("NeutrinoMC.root", "Untergrund_MC")

xsig = sig['x']
ysig = sig['y']
hsig = sig['AnzahlHits']

labsig = np.empty(len(xsig))


xbac = bac['x']
ybac = bac['y']
hbac = bac['AnzahlHits']

#labtrain = np.empty(10**4, dtype=object)#labelarray trainingsdatensatz
sig = np.array([xsig,ysig,hsig]).T
bac = np.array([xbac, ybac, hbac]).T
#training = np.append(sig[:5000],bac[:5000], axis=0)#erstellt trainingsdatensatz

training2 = np.append(sig[:500],bac[:500], axis=0)#erstellt trainingsdatensatz
labtrain2 = np.empty(1000, dtype=object)#erstellt labelarray
for q in range(0,1000):
    if (q<=500):
        labtrain2[q] = 's'
    else:
        labtrain2[q] = 'u'




#for q in range(0,10**4):
#    if (q<=5*10**3):
#        labtrain[q] = 's'
#    else:
#        labtrain[q] = 'u'




#testdata = np.append(sig[5000:15000], bac[5000:25000], axis=0)

#erstelle zu klassifizierenden datensatz 2000 untergrund und 1000 signalevents
#(leider benötigt das Programm bei uns mit der 10fachen datenmenge zu lange)
testdata2 = np.append(sig[500:1500], bac[500:2500], axis=0)

#wende knn an
#zahlsig,zahlbac = knnanwendung(training, labtrain,testdata,10)
zahlsig2, zahlbac2, res = knnanwendung(training2, labtrain2, testdata2,10)#hier wurden nachträglich zum generieren der Werte für f) 20 nachbarn eingesetzt
print("als signal klassifiziert: ", zahlsig2)
print("als untergrund klassifiziert: ", zahlbac2)

#reinheit etc
resulttsig = res[:1000]#echtes signal
resulttbac = res[1000:3000]#echter untergrund
tp = len(resulttsig[resulttsig == 's'])
tn = len(resulttbac[resulttbac == 'u'])
fp = len(resulttbac[resulttbac == 's'])
fn = len(resulttsig[resulttsig == 'u'])

rein   = tp/(tp+fp)
eff    = tp/(tp+fn)
signif = tp/(tn+tp+fp+fn)

print("reinheit: ", rein)
print("effizienz: ", eff)
print("signifikanz: ", signif)




#mit logarithmierten hits!
sigl = np.array([xsig,ysig,np.log10(hsig)]).T
bacl = np.array([xbac, ybac, np.log10(hbac)]).T

training2l = np.append(sig[:500],bac[:500], axis=0)#erstellt trainingsdatensatz
labtrain2l = np.empty(1000, dtype=object)#erstellt labelarray
for q in range(0,1000):
    if (q<=500):
        labtrain2l[q] = 's'
    else:
        labtrain2l[q] = 'u'

testdata2l = np.append(sig[500:1500], bac[500:2500], axis=0)

#wende knn an
zahlsig2l, zahlbac2l, resl = knnanwendung(training2l, labtrain2l, testdata2l,10)
print("\nals signal klassifiziert log hits: ", zahlsig2l)
print("als untergrund klassifiziert log hits: ", zahlbac2l)

#reinheit etc
resulttsigl = resl[:1000]#echtes signal
resulttbacl = resl[1000:3000]#echter untergrund
tpl = len(resulttsigl[resulttsigl == 's'])
tnl = len(resulttbacl[resulttbacl == 'u'])
fpl = len(resulttbacl[resulttbacl == 's'])
fnl = len(resulttsigl[resulttsigl == 'u'])

reinl   = tpl/(tpl+fpl)
effl    = tpl/(tpl+fnl)
signifl = tpl/(tnl+tpl+fpl+fnl)

print("reinheit log hits: ", reinl)
print("effizienz log hits: ", effl)
print("signifikanz log hits: ", signifl)
