from math import log
from scipy.optimize import minimize

def eu(x, W_h, r, H_j, t,k):
    sum = 0
    for j in range(t,t-k+2):
        sum += math.log((1-x)*W_h*(1 + r) + x*W_h*(1 + H_j))
    a_minimiser= (-sum)/k
    return a_minimiser

W_h=1000
r=0.04
H_j=[1,23,43,54]
bounds=[(0,100)]
X_0=[50]
t=22
k=15
minimization= float(minimize(eu, X_0, bounds=bounds, args =(W_h, r, H_j,t, k)).x)
print(minimization)