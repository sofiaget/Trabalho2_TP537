import numpy as np

#Com reposição

#Definindo listas de bolas de diferentes cores, cada uma com 10 elementos.
vermelho=['v','v','v','v','v','v','v','v','v','v']
azul=['az','az','az','az','az','az','az','az','az','az']
amarelo=['am','am','am','am','am','am','am','am','am','am']
roxo=['r','r','r','r','r','r','r','r','r','r']
#xx=vermelho.count('d')
#print(xx)

#Criando uma lista contendo todas as bolas de diferentes cores.
chapeu=azul+roxo+amarelo+vermelho #Colocando as listas em apenas uma

#Inicializando a variável de contagem como zero e definindo o número de amostras.
count=0
N=10000 #numero de amostras
for i in range(N):
    x=np.random.choice(chapeu, 10,replace=True) #Escolhe 10 valores da lista "chapeu", com reposição
    a=np.count_nonzero(x=='az')#conta quantos elementos são "az"
    r=np.count_nonzero(x=='r')#conta quantos elementos são "r"

    if a==2 and r==2: #Se tiver 2 elementos azuis e 2 elementos roxos será incrementado a variável contadora
        count=count+1

prob=count/N #Cálculo da probabilidade

print("a probabilidade de obter duas bolas azuis e duas bolas roxas em dez bolas sorteadas com reposiçao é",prob)


#####################################################################################################################


#Sem reposição

#Listas com 10 bolas de cada cor
vermelho=['v','v','v','v','v','v','v','v','v','v']
azul=['az','az','az','az','az','az','az','az','az','az']
amarelo=['am','am','am','am','am','am','am','am','am','am']
roxo=['r','r','r','r','r','r','r','r','r','r']
#xx=vermelho.count('d')
#print(xx)

chapeu=azul+roxo+amarelo+vermelho #Colocando as listas em apenas uma
count1=0
N=10000 #numero de amostras
for i in range(N):
    x=np.random.choice(chapeu, 10,replace=False) #Escolhe 10 valores da lista "chapeu", sem reposição
    a=np.count_nonzero(x=='az')#conta quantos elementos são "az"
    r=np.count_nonzero(x=='r')#conta quantos elementos são "r"

    if a==2 and r==2: #Se tiver 2 elementos azuis e 2 elementos roxos será incrementado a variável contadora
        count1=count1+1

prob1=count1/N #Cálculo da probabilidade

print("a probabilidade de obter duas bolas azuis e duas bolas roxas em dez bolas sorteadas sem reposiçao é",prob1)
