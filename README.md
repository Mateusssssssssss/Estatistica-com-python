# **Amostragem Simples com NumPy e Pandas**

## Descrição
Este script realiza uma **amostragem simples** utilizando as bibliotecas **NumPy** e **Pandas**. Ele carrega um conjunto de dados (Iris dataset) e cria uma nova amostra aleatória, onde os elementos são classificados em dois grupos distintos (0 e 1) com probabilidades definidas. Em seguida, um subconjunto do conjunto de dados é extraído com base nesses valores.

## Tecnologias utilizadas
- **Python**
- **Pandas** (para manipulação de dados)
- **NumPy** (para geração de amostras aleatórias)

## Funcionalidades
1. **Carregamento de Dados**: O dataset `iris.csv` é carregado.
2. **Definição da Semente Aleatória**: Utiliza `np.random.seed(2345)` para garantir reprodutibilidade dos resultados.
3. **Geração de Amostra Aleatória**:
   - Tamanho de **150 elementos**
   - Valores possíveis: **0 e 1**
   - Probabilidades associadas: **0 (70%) e 1 (30%)**
4. **Análise da Amostra Gerada**:
   - Conta quantas vezes **0** e **1** aparecem na amostra.
5. **Criação de um Novo Dataset**:
   - Filtra os valores do dataset original onde a amostra aleatória é **0**.

# -------------------------------------------------------------------------------------------------------------------------

# **Amostragem Sistematica com Python e Pandas**

Este script realiza uma amostragem aleatória de dados com base em uma população definida, utilizando o método de "sorteio sistemático". O código divide a população em subgrupos e seleciona elementos aleatórios para compor a amostra.

## **Objetivo**

O objetivo deste código é realizar a amostragem aleatória de dados de um conjunto de dados (como o dataset Iris). A amostra é gerada de forma sistemática, onde o primeiro valor é sorteado aleatoriamente e, em seguida, são sorteados outros valores com base em um incremento constante (k).

## **Tecnologias Utilizadas**
- **Python**: Linguagem de programação utilizada.
- **Pandas**: Biblioteca para manipulação de dados tabulares.
- **NumPy**: Biblioteca para geração de números aleatórios.
- **Math**: Utilizada para realizar o arredondamento de números para cima.

## **Como Funciona**

1. **Definição das variáveis**:
   - `populacao`: O tamanho da população total de dados (150 no exemplo).
   - `amostra`: O tamanho da amostra desejada (15 no exemplo).
   - `k`: Calculado com o valor `ceil(populacao / amostra)`, que define o incremento entre os elementos selecionados aleatoriamente.

2. **Sorteio aleatório**:
   - O código escolhe um número aleatório inicial dentro de um intervalo de 1 até `k + 1`.
   - Em seguida, cria-se um laço `for` que gera a amostra selecionando os índices com base no valor de `k` e acumulando o valor.

3. **Seleção da amostra**:
   - Usando os índices sorteados, o script carrega um conjunto de dados (exemplo: o dataset Iris) e seleciona as linhas que correspondem aos índices gerados aleatoriamente.

## **Passos do Código**

1. **Importação de Bibliotecas**:
   ```python
   import pandas as pd
   import numpy as np
   from math import ceil



#  -------------------------------------------------------------------------------------------------------------------------

# Exemplo de Uso de `train_test_split` com Estratificação

Este repositório demonstra como usar a função `train_test_split` da biblioteca `sklearn.model_selection` para dividir um dataset em amostras de treinamento e teste, preservando a distribuição das classes utilizando a estratificação. O código utiliza dois conjuntos de dados: **Iris** e **Infert**.

## Bibliotecas Utilizadas

- `pandas`: para carregar arquivos CSV e manipulação de dados.
- `sklearn.model_selection.train_test_split`: para dividir os dados em conjuntos de treinamento e teste de forma estratificada.

## Passos do Código

1. **Carregamento do Dataset Iris**
    O dataset Iris é carregado a partir de um arquivo CSV (`iris.csv`) e as classes (espécies da planta) são analisadas.

    ```python
    iris = pd.read_csv('iris.csv')
    print(iris)
    ```

2. **Visualização das Classes do Iris**
    É exibida a quantidade de registros por classe (espécie).

    ```python
    classes = iris['class'].value_counts()
    print(classes)
    ```

3. **Divisão dos Dados com Estratificação**
    A função `train_test_split` é usada para dividir o dataset em 50% para treino e 50% para teste, preservando a proporção das classes (utilizando a coluna `class` como referência para estratificação).

    ```python
    x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])
    qtd = y.value_counts()
    print(qtd)
    ```

    - `iris.iloc[:, 0:4]`: Seleciona as 4 primeiras colunas (atributos previsores).
    - `iris.iloc[:, 4]`: Seleciona a coluna de classes (espécie da planta).
    - `test_size=0.5`: Define que 50% dos dados serão usados para o teste.
    - `stratify=iris.iloc[:, 4]`: Preserva a proporção das classes na divisão.

4. **Carregamento do Dataset Infert**
    O dataset Infert é carregado a partir de um arquivo CSV (`infert.csv`).

    ```python
    infert = pd.read_csv('infert.csv')
    print(infert)
    ```

5. **Visualização das Classes do Infert**
    Exibe a quantidade de registros por classe na coluna `education`.

    ```python
    educação = infert['education'].value_counts()
    print(educação)
    ```

6. **Divisão dos Dados com Estratificação no Infert**
    A função `train_test_split` também é usada no dataset Infert, mas com a divisão em 40% para o teste (60% para treino), e a estratificação é realizada com base na coluna `education`.

    ```python
    x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=0.6, stratify=infert.iloc[:, 1])
    qtd1 = y1.value_counts()
    print(qtd1)
    ```

    - `infert.iloc[:, 2:9]`: Seleciona as colunas de índice 2 a 8 (atributos previsores).
    - `infert.iloc[:, 1]`: Seleciona a coluna `education` para estratificação.
    - `test_size=0.6`: Define que 60% dos dados serão usados para o teste.



 




