import pandas as pd
import numpy as np
#Ceil "empurra" o número para cima, para o próximo inteiro maior
from math import ceil
#Criação de variaveis para representar população, amostra e valor de k
populacao = 150
amostra = 15
k = ceil(populacao / amostra)
# k = 10
print(k)

#Definição  do valor  randomico para inicializar a amostra, iniciando em 1 até  k + 1.
r = np.random.randint(low= 1, high= k + 1, size= 1)
print(r)
#FFor criado para somar os proximos valores, baseado no primeiro valor r que foi definido acima
acumulador = r[0]
sorteados = []
for i in range(amostra):
    sorteados.append(int(acumulador))
    acumulador += k
    
print(sorteados)
#Carregando o dataset e criando um novo baseado na aleatoriedade de amostras feitas a cima
data = pd.read_csv('iris.csv')
print(data)
data_new = data.loc[sorteados]
print(data_new)