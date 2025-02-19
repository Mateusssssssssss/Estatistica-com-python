from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
#Criação de uma variavel com dados, em uma distribuição normal  com a função rvs(1000 elementos)
dados = norm.rvs(size=1000)
print(dados)
# Tamanho dos dados
tamanho = len(dados)
print(tamanho)
#histograma
plt.hist(dados, bins = 20)
plt.title('Dados')
plt.show()

#Geração de grafico para verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados, fit=True, plot=ax)
plt.show()

#teste de shapiro(teste de hipotese)
#segundo o argumento é o valor de p, não há como rejeitar a hipotese nula.
#Interpretação do valor-p (p-value):
# p > 0,05 → Aceita a hipótese nula (Os dados são normalmente distribuídos).
# p ≤ 0,05 → Rejeita a hipótese nula (Os dados não são normalmente distribuídos).
shapiro1 = stats.shapiro(dados)
print(shapiro1)