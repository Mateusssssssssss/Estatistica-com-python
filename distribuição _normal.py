#Probabilidade, Tabela Z
from scipy.stats import norm

#Conjunto de objetos em uma cesta, onde a media é 8, desvio padrao é 2
#Qual a probabilidade de se tirar um objeto que o peso é menor que 6 quilos?
# Ou seja, há aproximadamente 15,87% de chance da variável aleatória assumir um valor entre 8 e 10.
z = norm.cdf(6,8,2)
print(round(z,4))

#Qual a Probabilidade de tirar um objeto que o peso é maior que 6 quilos
# Ou seja, há aproximadamente 84,13% de chance da variável aleatória assumir um valor entre 8 e 10.
z1 = norm.sf(6,8,2)
print(round(z1,4))
#ou 
# z2 = 1 - norm.cdf(6,8,2)
# print(round(z2, 4))

#Probabilidade de tirar um objeto com peso menor que 6 ou maior que 10
# Ou seja, há aproximadamente 31,73% de chance da variável aleatória assumir um valor entre 8 e 10.
prob = norm.cdf(6,8,2) + norm.sf(10,8,2)
print(prob)

#Probabilidade de tirar um objeto com peso menor que 10 ou maior que 8
prob1 = norm.cdf(10,8,2) - norm.cdf(8,8,2)
print(prob1)
#Ou seja, há aproximadamente 34,13% de chance da variável aleatória assumir um valor entre 8 e 10.
