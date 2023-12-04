# Ponderada 5

Nesta ponderada, foi conduzido um diálogo entre LMM e RAG, onde as respostas oferecidas foram fundamentadas em um documento específico. No presente caso, optou-se por um site que disponibilizava diretrizes de segurança no contexto industrial.
Para realizar essa interação, a equipe empregou a biblioteca langchain para carregar o conteúdo do referido site e transformá-lo em vetores. Esses vetores foram posteriormente utilizados no prompt do modelo Ollama. A etapa subsequente envolveu a implementação do Gradio, proporcionando uma experiência visual do diálogo por meio de uma interface gráfica interativa.

## Manual

1. Para baixar tudo que é necessário utilize:
```
pip install -r requirements.txt
```
2. Inicie o modelo que utilizaremos para que ele seja baixado no computador:
```
ollama run mistral
```
3. Inicie o script:
```
gradio chat.py
```
4. Isso disponibilizará um link para a interface.

## Demonstração
[Gradio.webm](https://github.com/gio-rodrigues0/ponderadas_m8/assets/99195612/98d8f492-ef7b-4b28-9039-1464e6f408a6)
