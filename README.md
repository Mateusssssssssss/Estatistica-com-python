# README - Amostragem Simples com NumPy e Pandas

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



