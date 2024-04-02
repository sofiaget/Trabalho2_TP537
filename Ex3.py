import numpy as np

#Com reposição

valor=9 #soma das 4 faces tem que ser menor que 9
faces=[1,2,3,4,5,6] #faces do dado
N=1000 #jogadas

carteira=0


for i in range(N):
    x=np.random.choice(faces, 4,replace=True) #Escolhe 4 faces, simulando 4 jogadas de ados
    soma=np.sum(x)

    if soma<9: #Se tiver 2 elementos azuis e 2 elementos roxos será incrementado a variável contadora
        carteira=carteira-1+10

    else:
        carteira=carteira-1

#verificar se é positivo e negativo, colocar dois prints com condição.

if carteira>0:
    print("a longo prazo,depois de",N,"jogadas, ele ganhará",carteira, "reais")

else:
    carteira=carteira*-1
    print("a longo prazo, depois de",N,"jogadas, ele perderá",carteira, "reais")