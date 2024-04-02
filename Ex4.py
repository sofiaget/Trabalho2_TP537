import numpy as np
import math
import matplotlib.pyplot as plt

# a)
#Integração de monte carlo
N=100000
y=np.random.uniform(0,1,N) #Geração de uma distribuição uniforme de 0 a 1
integrala=1*sum(pow((1-y**2),3/2))/N # Calcula o somatório e depois divide por N (Valor esperado)
print(integrala)

#Integração por importância

N=100000
y=np.random.uniform(0,1,N) #Geração de uma distribuição uniforme de 0 a 1
ygen=pow(y,1/3); #Geração de ygen pelo metodo da inversa
integrala1=sum(pow((1-ygen**2),3/2)/(3*ygen**2))/N; # Calcula o somatório e depois divide por N (Valor esperado)
print(integrala1)
######################################################################################################################
# b)
#Integração de monte carlo
N=100000
y=np.random.uniform(0,1,N)
integralb=4*sum(np.exp((4*y-2) + pow((4*y-2),2)))/N
print(integralb)

#Integração por importância

N=100000
y=np.random.uniform(0,1,N)
ygen=np.log(y*(np.exp(2)-np.exp(-2))+np.exp(-2))
integralb1=sum(np.exp(ygen+ygen**2)/((np.exp(ygen))/(np.exp(2)-np.exp(-2))))/N
print(integralb1)

######################################################################################################################
# c)
#Integração de monte carlo
N=100000
y=np.random.uniform(0,1,N)
integralc=sum((y**-2)*(1/y-1)*pow((1+(pow(1/y-1,2))),-2))/N
print(integralc)

#Integração por importância

N=100000
y=np.random.uniform(0,1,N)
ygen=np.sqrt(y)
integralc1=sum(((ygen**-2)*(1/ygen-1)*pow((1+(pow(1/ygen-1,2))),-2))/(2*ygen))/N
print(integralc1)