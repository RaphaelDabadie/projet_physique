

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
