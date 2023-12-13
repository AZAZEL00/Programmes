import numpy as np
import matplotlib.pyplot as plt 
import math

# definition de la prevalence 
def prevalence(alpha, delta, beta, d, tau, r, gamma,mu,rho,I0,N0):
 
    I = (mu * (1-d)/ rho*beta+1)*N0 - 1 - (mu*(1-d)/rho*beta +1) - ((alpha *gamma + (tau +alpha*(1-gamma)*(d+delta*(1-d))))/alpha+tau)*I0
    N = (1+r-d)*N0 - (((1-d)*(delta*(delta*(alpha+tau))+ alpha*gamma*(1-delta)))/alpha + tau)*I0
   
    return I,N
#I = [].append(In)
#N = [].append(Nn)

 # definition des parametres de la prevalence
alpha = 0.5
delta = 0.5
beta = 1
d = 0.5
tau = 10
r = 0.5
gamma = 0.3
mu = 13
rho = 12
N0 = 5
I0 = 1
t = np.linspace(0, 10, 10)

I = []
N = []
P = []
for i in range(10):
    i, n = prevalence(alpha, delta, beta, d, tau, r, gamma,mu,rho,I0,N0)
    p = i / n

    i = round(i, 2)
    n = round(n, 2)
    p = round(p, 2)

    P.append(p)
    I.append(i)
    N.append(n)
    I0 = i
    NO = n




#determiner le temps
print(I)
print(N)
print(P)





# operation de la prevalence
#I,N = prevalence(alpha, delta, beta, d, tau, r, gamma) 
#result = [ I/N ]
#print(I)
#print('prevalence')
#rint ('I[2]')
plt.plot(P, label="p")
#plt.plot(I, label="I")
#plt.plot(N, label="N")
plt.legend()
plt.show()