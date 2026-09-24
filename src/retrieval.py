from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.vector_store import initialize_vector_store

class Retrieval:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve_evidence(self, query, top_k=5):
        return self.vector_store.query(query, top_k=top_k)

    def load_documents(self, document_paths):
        documents = []
        documents.extend(document_paths)
        return documents

    def chunk_documents(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return text_splitter.split_documents(documents)

    def index_documents(self, documents):
        chunks = self.chunk_documents(documents)
        self.vector_store.store.add_documents(chunks)

    def query(self, query_text, top_k=5):
        return self.retrieve_evidence(query_text, top_k=top_k)


def retrieve_evidence(query, top_k=5, vector_store=None):
    """Retrieve LangChain documents with their source metadata preserved."""
    store = vector_store or initialize_vector_store()
    return Retrieval(store).retrieve_evidence(query, top_k=top_k)