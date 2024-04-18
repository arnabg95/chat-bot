from langchain_openai import OpenAIEmbeddings
from app.config.settings import settings
from langchain_pinecone import PineconeVectorStore



embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

index_name = settings.PINECONE_INDEX_NAME

def get_vector_store():
    """create and return vector store retriver"""
    return PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings,
        pinecone_api_key=settings.PINECONE_API_KEY
    ).as_retriever(k=5)


def find_documents(query:str):
    """find and return nearby documents"""
    retriever = get_vector_store()
    # qa = get_retriver(retriever=retriever)
    # answer = qa.invoke(input=query)
    # return answer['result']
    print(query)
    return retriever.get_relevant_documents(query)