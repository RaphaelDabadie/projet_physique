# definition des fonctions
from math import log
from scipy.optimize import minimize

def eu(x, W_h, r, H_j, t,k): # fonction d'utilité à maximiser
    sum = 0
    for j in range(t,t-k+2):
        sum += math.log((1-x)*W_h*(1 + r) + x*W_h*(1 + H_j))
    a_minimiser= (-sum)/k
    return a_minimiser

def cycle(X_0, D_t, P_t, W_t, N_t, H_k, k, r, t): # donne l'étape t+1 à partir de l'étape t pour l'investisseur i
    W_t_new= W_t + N_t*D_t + (W_t - N_t*P_t)*r # Retour sur investissement avant échange
    P_h = 12 # Prix attendu - à compléter
    W_h = W_t_new + N_t*D_t + (W_t_new - N_t*P_t)*r + N_t*(P_h - P_t) # Richesse attendue
    EU=eu(X_0, W_h, r, H_j, t, k) # Fonction d'utilité à maximiser
    X_h = float(minimize(eu, X_0, bounds=bounds, args =(W_h, r, H_j,t, k)).x) # argmax de la fonction
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
H_k=[1,23,43,54] # des valeurs arbitraires et pas données dans l'article
k=15
r=0.04
t=12 # idem
print(cycle(X_0, D_0, P_0, W_0, N_0, H_k, k, r, t))