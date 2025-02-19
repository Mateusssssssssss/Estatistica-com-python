#Bibliotecas
from scipy import stats
import numpy as np
#Criação da variavel com os dados dos jogadores, visualização da mediana e média
jogadores = [4000, 6000, 7000, 9000, 4500, 20000, 15000, 12000, 13000]
#Media de salario dos jogadores
media = np.mean(jogadores)
#round usado para limitar o numero de casas decimais.
print(round(media, 2))
#mediana
mediana = np.median(jogadores)
print(mediana)

#criação da variavel para geração de quartis(0%, 25%, 50% e 100%)
quartis = np.quantile(jogadores,[0, 0.25, 0.5, 0.75, 1])
print(quartis)
 #Calculo desvio padrão, ddof ajusta o desvio para a amostra e não para a população total aplicando a correção de Bessel.
desvio = np.std(jogadores,ddof=1)
print(round(desvio, 3))
#stats metodo estatistico que exibi alguns resultados, como min e max, nobs, media, variancia, etc
q = stats.describe(jogadores)
print(q)

