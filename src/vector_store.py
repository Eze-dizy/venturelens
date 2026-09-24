from pathlib import Path

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


class VectorStore:
    def __init__(self, db_path, api_key=None):
        self.embeddings = OpenAIEmbeddings(api_key=api_key, model="text-embedding-3-small")
        self.store = Chroma(
            collection_name="startup_embeddings",
            persist_directory=str(Path(db_path)),
            embedding_function=self.embeddings,
        )

    def add_documents(self, documents):
        langchain_documents = [
            Document(page_content=item["text"], metadata=item.get("metadata", {}))
            for item in documents
        ]
        if langchain_documents:
            self.store.add_documents(langchain_documents)

    def query(self, query_text, top_k=5):
        return self.store.similarity_search(query_text, k=top_k)

    def clear(self):
        self.store.delete_collection()


def initialize_vector_store(config=None):
    from src.config import load_config

    config = config or load_config()
    return VectorStore(config["chroma_dir"], api_key=config["openai_api_key"] or None)