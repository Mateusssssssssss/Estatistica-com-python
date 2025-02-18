import pandas as pd
import numpy as np

#AMOSTRAGEM SIMPLES
data = pd.read_csv("iris.csv")
data.shape
print(data)
#Mudança da semente aleatoria para manter os resultados em varias execuções
np.random.seed(2345)
#150 amostras de 0 a 1, com reposição, probabilidades equivalentes.
amostra = np.random.choice(a = [0, 1], size=150, replace=True, p = [0.7, 0.3])
print(amostra)
#verificando tamanho da amostra
tamanho = len(amostra)
print(tamanho)
#Quantas vez 0 e 1 apareceram
prob0 = len(amostra[amostra == 0] )
prob1 = len(amostra[amostra == 1])
print(f'Vezes que o 0 apareceu: {prob0}')
print(f'Vezes que o 1 apareceu: {prob1}')
#Amostragem, novo dataset criado aleatoriamente onde a valores 0
data_new = data.loc[amostra == 0]
print(data_new)
