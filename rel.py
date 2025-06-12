import google.generativeai as genai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai
import google.auth

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai

class DocumentRetriever:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        credentials, project = google.auth.default()
        self.model = genai.GenerativeModel('text-embedding-004')

        genai.configure(api_key=None, credentials=credentials)
        self.chunks = []
        self.embeddings = []
        
    def process_document(self):
        # Load and split document
        loader = PyPDFLoader(self.pdf_path)
        pages = loader.load()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.chunks = splitter.split_documents(pages)
        
        # Generate embeddings for all chunks using the correct method
        for chunk in self.chunks:
            result = self.model.cached_content(chunk.page_content)
            self.embeddings.append(result.embeddings)

retriever = DocumentRetriever(
    pdf_path="/Users/thevedantsingh/Desktop/SLS/relevant.pdf"
)

# Process the document
retriever.process_document()

# Get relevant chunks
chunks = retriever.get_relevant_chunks(
    query="4329. Affirmative Defense—Failure to Provide Reasonable Accommodation",
    k=5
)

# Print results
for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i}:")
    print(chunk)
