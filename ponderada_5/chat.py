from langchain.document_transformers import BeautifulSoupTransformer
from langchain.document_loaders import AsyncHtmlLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import GPT4AllEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.llms import Ollama
from langchain.schema.runnable import RunnablePassthrough
import gradio as gr
import time

url = "https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety"
loader = AsyncHtmlLoader(url)
docs = loader.load()

bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(docs, tags_to_extract=['main'], unwanted_tags=['footer'])

docs_text = docs_transformed[0].page_content[2330:6090]

vectorstore = FAISS.from_texts(
    [docs_text], embedding=GPT4AllEmbeddings()
)
retriever = vectorstore.as_retriever()

print(retriever)

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="mistral")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        for s in chain.stream(message):
            bot_message += s
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
