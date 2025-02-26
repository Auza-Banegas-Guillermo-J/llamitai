from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

import os

def load_documents(path="./docs/txt/"):
    loader = DirectoryLoader(path, glob="*.txt")
    docs = loader.load()
    return docs

def chunk_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500, 
        chunk_overlap = 125,
        length_function = len,
        add_start_index = True,
        )
    chunks = text_splitter.split_documents(docs)
    return chunks

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_key(route="./.key.txt"):
    with open(".key.txt") as key_file:
        key = key_file.read().strip()
    return key

def init_module(chroma_dir = "./chroma_db"):
    os.makedirs(chroma_dir, exist_ok=True)
    
    my_api_key = get_key()

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key = my_api_key,
    )

    if os.path.exists(chroma_dir) and len(os.listdir(chroma_dir)) > 0:
        vectorstore = Chroma(persist_directory = chroma_dir, embedding_function = embedding_model)
    else:
        documents = load_documents()
        chunks = chunk_splitter(documents)
        vectorstore = Chroma.from_documents(
            documents = chunks, 
            embedding = embedding_model,
            persist_directory = chroma_dir
        )
    
    model = ChatOpenAI(
        model = "gpt-4o",
        temperature = 0,
        max_tokens = None,
        timeout = None,
        max_retries = 1,
        api_key = my_api_key
    )
    
    template = """Responde a la peticion cubierto en llaves de manera simple y concisa.
    Para esta tarea utiliza el contexto en sus llaves correspondientes.
    <contexto>
    contexto : {context}
    </contexto>
    <peticion>
    peticion: {question}
    </peticion>
    """
    return vectorstore, model, template

def get_answer(question,template,vectorstore,model):
    docs = vectorstore.similarity_search(question)
    context = format_docs(docs)

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    response = chain.invoke({"context": context, "question": question})

    print(question+"\n\n"+context+"\n\n")

    return response.content

if __name__ == "__main__":

    vectorstore, model, template = init_module()

    question = """¿Quiénes son los demandados?
    ¿Quiénes son los demandantes?
    ¿Quién es el juez encargado del caso?
    ¿Que tipo de proceso es este?
    ¿Cuando y donde sucedio la demanda?"""

    response = get_answer(question=question, template=template, vectorstore=vectorstore, model=model)

    print(response)