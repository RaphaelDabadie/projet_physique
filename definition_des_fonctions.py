# definition des fonctions
from math import log

def cycle(X_t, D_t, P_t, W_t, N_t, H_k, k, r, t): # donne l'étape t+1 à partir de l'étape t pour l'investisseur i
    W_t_new= W_t + N_t*D_t + (W_t - N_t*P_t)*r # Retour sur investissement avant échange
    P_h = 12 # Prix attendu - à compléter
    W_h = W_t_new + N_t*D_t + (W_t_new - N_t*P_t)*r + N_t*(P_h - P_t) # Richesse attendue
    EU=0
    for j in range (1, t-k+1):
        EU = EU + log( (1-X_t)*W_h*(1+r) + X_t*W_h*(1+H_k[j]))
    EU=EU/k # Fonction d'utilité espérée
    X_h = 0 # Maximisation de la fonction EU - à faire
    N_h= (X_h*W_h)/P_h # Définition de la courbe de demande
    P_t_future= (X_h*W_h)*10000 # Prix à t+1
    D_t_new=D_t + 0.05*D_t # Dividende à t+1
    H_new= (P_t_future - P_t + D_t_new)/P_t # Retour sur investissement à t+1
    H_k.append(H_new) # Mise à jour de la mémoire de l'investisseur
    H_k=H_k[1: len(H_k)] # Mise à jour de la mémoire de l'investisseur
    return P_t_future, H_k

# test
X_0=0.50
W_0=1000
P_0=4.00
N_0=100
D_0=0.20
H_k=[1,23,43,54]
k=15
r=0.04
t=12
print(cycle(X_0, D_0, P_0, W_0, N_0, H_k, k, r, 2))

"""
# definition des fonctions

def dividende(T): # calcule les T premières valeurs des dividendes (Dt)
    D0=0.20
    for i in range(T):
        D.append(D0(1+0.05)**i)
    return D


def portemonnaie(T, P): # Calcule Wt
    W=[1000]
    D=dividende(T)
    for i in range(T):
        W.append(W[i]+D[i]*10+(W[i]-10*P[i])*0.04+10(P-P[i]))
    return W

def N(T,p): # Calcule Nt
    N=[50]
    for i in range(T):
        N.append(X[i]*W[i]/p)
    return N

def fonction(T,p): # reprend les fonctions créées précédemment
    W=[1000]
    N=[50]
    P=[4.00]
    X=[]
    D=[0.2]
    t=0
    while t < T:
        D.append(D0(1+0.05)**t)
        W.append(W[t]+D[t]*10+(W[t]-10*P[t])*0.04+10(P-P[t]))
        N.append(W[t]+D[t]*10+(W[t]-10*P[t])*0.04+10(P-P[t])*argmax(...)/p)
        X.append(argmax(...))
        t+=1
"""