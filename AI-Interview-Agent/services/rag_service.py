from utils.parser import PDFParser
from utils.rag import VectorStore


class RAGService:

    @staticmethod
    def process_pdf(file_path):

        text = PDFParser.extract_text(file_path)

        chunks = VectorStore.create(text)

        return {

            "message": "Vector Database Created",

            "chunks": chunks

        }