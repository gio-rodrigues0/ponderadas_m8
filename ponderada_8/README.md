# Ponderada 8

Nesta ponderada, as tecnologias de Reconhecimento de Fala (STT) e Síntese de Fala (TTS) da OpenAI foram empregadas para realizar as seguintes etapas: transcrição de um áudio, tradução para o inglês e subsequente reprodução do conteúdo.

1. Gravar um arquivo de entrada.
2. Utilizar essa gravação no Whisper, que realiza a transcrição e tradução.
3. Enviar o texto resultante para o TTS, que cria um novo arquivo de áudio com a tradução.

## Como executar

1. É necessário instalar as dependências:
```
pip install -r requirements.txt
```

2. Criar um arquivo .env com a variável de ambiente correspondendo à uma chave de API da OpenAI

3. Execute o comando:
```
python tradutor.py
```

## Demonstração
https://github.com/gio-rodrigues0/ponderadas_m8/assets/99195612/cb3a46e5-b910-4355-8be4-7fc8bf8bc810

