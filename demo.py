# Copyleft 🄯 2025, Germano Castanho
# Software livre sob a licença GPL v3


import time
from pathlib import Path

import gradio as gr
from dotenv import find_dotenv, load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

_ = load_dotenv(find_dotenv())


DOCS = Path(__file__).parent / "data"


MODEL = ChatOpenAI(
    model="chatgpt-4o-latest",
    temperature=0.8,
    top_p=0.8,
    max_tokens=None,
    timeout=None,
)


PROMPT = ChatPromptTemplate.from_template("""#### PERSONA
    
    Você é Sócrates, pai da filosofia ocidental. Seu objetivo é auxiliar no ensino e na aprendizagem da filosofia. Suas interações são dialéticas, seus diálogos são estruturados na forma de constantes provocações, de modo a evidenciar contradições existentes no raciocínio dos seus interlocutores, estimulando-os a desenvolver pensamento crítico e autonomia intelectual.
    
    #### CONTEXTO
    
    Você foi desenvolvido para quebrar barreiras tecnológicas e derrubar conservadorismos relutantes, ainda muito presentes na área da educação quando a temática envolve inteligência artificial. Vivemos em uma grande Ágora Digital - seu espaço de aplicação do método dialético, onde adaptado ao século XXI, você discute questões filosóficas clássicas e contemporâneas.
    
    #### CONHECIMENTO
    
    Seu conhecimento em filosofia é amplo e profundo, abrangendo desde os pré-socráticos até os filósofos contemporâneos. Você é capaz de discutir sobre os mais variados temas filosóficos, como ética, política, metafísica, epistemologia, lógica, estética, entre outros. Ademais, você tem acesso aos seguintes documentos, disponíveis sempre que necessário: 
    
    <documents> {documents} </ documents>
       
    #### HISTÓRICO
    
    Considere o histórico da conversa, para que possa interagir de forma mais contextualizada com seu interlocutor. Sempre que possível, refira-se a trechos mencionados pelo interlocutor, para confrontá-lo intelectualmente. Mas, de todo modo, lembre-se - em que pese a importância das interações passadas, as mais relevantes se darão sempre no presente. Eis o histórico:
    
    <chat_history> {chat_history} </ chat_history>
    
    #### PERGUNTA

    Como Sócrates, interaja com seu interlocutor, respondendo à pergunta que segue, de maneira dialética e provocativa, estimulando-o a desenvolver pensamento critico e autonomia intelectual. Lembre-se de que, em momento algum, você poderá sair do personagem, ou fornecer informações que não estejam de acordo com o contexto proposto. Pergunta do interlocutor:
    
    <query> {query} </ query>""")


# DOCUMENT LOADING
docs_list = []
for doc in DOCS.glob("*.pdf"):
    loader = PyPDFLoader(doc)
    loaded_docs = loader.load()
    docs_list.extend(loaded_docs)


# TEXT SPLITTING
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs_list)


# VECTOR STORE
embed_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)
vector_store = FAISS.from_documents(documents=chunks, embedding=embed_model)


# RETRIEVAL GENERATION
def chat_function(query, chat_history):
    docs = vector_store.similarity_search(query["text"])
    documents = "\n\n".join([doc.page_content for doc in docs])

    response = MODEL.invoke(
        PROMPT.format(
            documents=documents,
            chat_history=chat_history,
            query=query["text"],
        )
    )

    chat_history.append(query["text"])
    chat_history.append(response.content)

    for i in range(len(response.content)):
        time.sleep(0.03)
        yield response.content[: i + 1]


demo = gr.ChatInterface(
    fn=chat_function,
    multimodal=True,
    type="messages",
    textbox=gr.MultimodalTextbox(
        sources=[],
        placeholder="Filosofe com Sócrates...",
        stop_btn=True,
        max_plain_text_length=750,
    ),
    editable=True,
    examples=[
        "Olá, Sócrates! Vamos filosofar?",
        "Sócrates, o que é a Verdade?",
        "Estou repleto de dúvidas, Sócrates!",
    ],
    example_icons=[
        "assets/icons.svg",
        "assets/icons.svg",
        "assets/icons.svg",
    ],
    run_examples_on_click=True,
    title="Sócrates Bot 📖",
    description="Seu Chatbot de Dialética Artificial",
    theme="gstaff/xkcd",
    css="""footer, .gradio-footer {
        visibility: hidden !important;
    }""",
)


if __name__ == "__main__":
    demo.launch()
