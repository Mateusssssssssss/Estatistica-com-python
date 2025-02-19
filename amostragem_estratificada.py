# Importação das bibliotecas: pandas para carregar arquivos csv e train_test_split para divisão
# da base de dados(separar amostras)
import pandas as pd
from sklearn.model_selection import train_test_split
#Carregar o csv
iris = pd.read_csv('iris.csv')
print(iris)
#Quantidade por Classes
classes = iris['class'].value_counts()
print(classes)
#Iris.iloc[: , 0:4]: Busca somente atributos previsores, ou seja, os dados sobre pétala e sétala da planta
#Iris.iloc[:, 4] Busca somente a classe, que é a especie da planta (setosa, viriginica ou versicolor)
#test_size: Seleciona apenas 50% da base de dados, que serão copiados para as variaveis x e y. essa função retorna4 valores,
#porem, vamos usar somente os 50%  da base de dados  e por isso  colocamos  'underlines' para outros valores x, "_', y, "_"
#stratify: para retornar a amostra baseada na classe
#(iris.iloc[:, 0:4] → Seleciona as 4 primeiras colunas (as features do dataset).
# iris.iloc[:, 4] → Seleciona a 5ª coluna (os rótulos/classes das flores).
# test_size=0.5 → Define que 50% dos dados serão usados como conjunto de teste.
# stratify=iris.iloc[:, 4] → Garante que a divisão preserve a proporção das classes.)
x, _, y, _ = train_test_split(iris.iloc[:,0:4], iris.iloc[:, 4], test_size= 0.5, stratify=iris.iloc[:, 4])

qtd = y.value_counts()
print(qtd)


#Outro dataset
infert = pd.read_csv('infert.csv')
print(infert)

educação = infert['education'].value_counts()
print(educação)
#criando uma amostra com apenas 40% dos registros(por isso é definido 0.6, pois é gerado o inverso)
x1, _, y1, _ = train_test_split(infert.iloc[:,2:9], infert.iloc[:, 1], test_size= 0.6, stratify=infert.iloc[:, 1])
qtd1 = y1.value_counts()
print(qtd1)

