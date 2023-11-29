# Ponderada 6

O código desempenha a função de determinar os pesos e o viés associados a cada entrada do perceptron. Nesse processo, para cada conjunto de valores de entrada e saída fornecidos, realizamos uma previsão utilizando nosso método de predição. Em seguida, calculamos o erro, que representa a diferença entre o valor real e o valor previsto. Os pesos e o viés são, então, atualizados com base nesse erro.

Além disso, as entradas e saídas fornecidas correspondem às operações lógicas AND, OR, NAND e XOR. Isso permite que o perceptron ajuste seus pesos e viés, capacitando-o a inferir os valores da tabela verdade associada a cada uma dessas operações lógicas. O método funcionou adequadamente para todas as portas lógicas, com exceção da XOR. Isso ocorre porque o problema da XOR não é linear, impossibilitando que um único perceptron resolva eficientemente essa operação. Esse desafio destaca a limitação dos perceptrons em abordar problemas não lineares de forma isolada.

## Para rodar o script:

De acordo com a porta lógica que será testada, seus inputs (x e y) deverão ser descomentados.

Depois, apenas rode o arquivo script com:

```
python perceptron.py
```