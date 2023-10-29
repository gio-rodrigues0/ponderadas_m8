# Ponderada 1

## O robô deve manter uma margem de segurança de 5 cm.

O requisito funcional escolhido determina que o robô deve manter uma distância mínima de 5 cm de qualquer objeto que possui a altura mínima do sensor Lidar. Sendo essencial para garantir uma operação segura e a proteção tanto do robô quanto de objetos do ambiente.

## Testes

Para testar a eficácia desse requisito, uma série de métodos de teste foi desenvolvida para abranger diversas situações:

### Testes de Posicionamento Diversificado:

Uma abordagem crucial para avaliar a eficiência do requisito é conduzir múltiplas rodadas de teste com posicionamentos variados de obstáculos em relação ao caminho do robô. Além disso, é recomendável criar uma marcação visual de um raio de 5 cm em torno dos objetos para facilitar a detecção de violações. O cálculo da eficiência do sistema de desvio pode ser obtido ao dividir o número de testes bem-sucedidos pelo número total de testes realizados.

### Teste de Variação de Velocidade:

É importante avaliar se o robô consegue manter a margem de segurança de 5 cm em diferentes velocidades de movimento. Repetir o teste anterior com variações na velocidade do robô ajudará a determinar se ele ainda é capaz de se movimentar de forma segura, respeitando a margem de proximidade, independentemente da velocidade. Depois, é de suma importância, registrar quais velocidades mais se adequam ao equilíbrio entre segurança e eficiência operacional.

### Teste de Objetos Inesperados e em Movimento:

Introduzir objetos inesperados e móveis no ambiente de teste é crucial para avaliar a capacidade de reação do robô. Isso permitirá verificar se o robô pode desviar de maneira eficaz respeitando a margem de segurança em cenários dinâmicos. Além disso, esses testes ajudarão a identificar a rapidez com que o robô responde a novos obstáculos inesperados. Durante os testes, marcações visuais também devem ser feitas, com metas de proximidades, podendo determinar até qual proximidade mínima da margem de segurança o robô é capaz de reagir a objetos inesperados.

Esses métodos de teste abrangentes asseguram que o robô atenda ao requisito de margem de segurança de 5 cm de maneira consistente e segura, independentemente das condições, contribuindo para um funcionamento confiável em ambientes variados e imprevisíveis.