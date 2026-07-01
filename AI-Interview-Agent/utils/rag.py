from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from utils.embeddings import get_embeddings


class VectorStore:

    @staticmethod
    def create(text):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_text(text)

        embeddings = get_embeddings()

        db = FAISS.from_texts(
            chunks,
            embeddings
        )

        db.save_local("vectorstore")

        return len(chunks)


class Retriever:

    @staticmethod
    def search(question):

        embeddings = get_embeddings()

        db = FAISS.load_local(
            "vectorstore",
            embeddings,
            allow_dangerous_deserialization=True
        )

        docs = db.similarity_search(
            question,
            k=3
        )

        return docs