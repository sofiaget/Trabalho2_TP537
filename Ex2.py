# Distribuição binomial

import numpy as np

q=1/6 #Probabilidade de sair a face 6 em um dado
n=5 #Número de jogadas
value1=1 #pelo menos 1 dado com face 6
N=100000#Número de amostras
c = q/(1-q)
av=np.array([])
count=0
x=np.random.uniform(0,1,N)#Geração de uma distribuição uniforme de 0 a 1

for ix in x:
    i = 0
    pr = pow((1 - q),n)
    F = pr
    while ix>=F:
        pr = (c * (n - i) / (i + 1))* pr;
        F = F + pr;
        i = i + 1;
    a1=i
    av=np.append(av,a1)

print(av)

for binvalue in av:
    if binvalue>=value1: #Para x>=1. Para a probabilidade de pelo menos 1 dado com face 6
        count=count+1
prob=count/N
print("a probabilidade sair pelo menos um dado com face seis em cinco jogadas é",prob)