# Ponderada 7

Nesta ponderada, desenvolvemos uma rede neural convolucional dedicada à classificação de números com base no conjunto de dados MNIST.

## Etapas Realizadas:

1. Carregamento do Conjunto de Dados MNIST: O conjunto de dados MNIST foi carregado para treinar e testar a rede neural.

2. Divisão dos Dados de Treino e Teste: Os dados de entrada e saída foram divididos em conjuntos de treino e teste.

3. Criação do Modelo Sequencial: Um modelo sequencial foi criado para facilitar a configuração da arquitetura da rede.

4. Adição da Camada de Entrada: Uma camada de entrada foi adicionada para receber os dados.

5. Camadas Densas com ReLU: Foram adicionadas camadas densas com 128 neurônios cada, utilizando a função de ativação ReLU.

6. Camada de Saída com Softmax: A camada de saída foi configurada com 10 neurônios e a função de ativação softmax.

7. Compilação do Modelo: O modelo foi compilado com parâmetros escolhidos para otimização, função de perda e métricas.

8. Treinamento do Modelo: O treinamento foi realizado ao longo de 3 épocas, sendo suficiente para alcançar uma acurácia superior a 95%.

9. Avaliação do Modelo: Foram calculados os valores de perda e acurácia para avaliar o desempenho da rede neural.

## Como utilizar:

Para fazer classificação de um valor, utilize:
```
prediction = classifier.predict([x_test[0]])
```

Para melhor visualização:
```
import numpy as np

print(np.argmax(prediction))
```

## Demonstração
[ponderada7.webm](https://github.com/gio-rodrigues0/ponderadas_m8/assets/99195612/dc95cab7-96cb-4c00-aa79-aa0138b8490b)

