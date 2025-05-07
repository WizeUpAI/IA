from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
# Initialize embeddings
embeddings = OpenAIEmbeddings()
# Create vector store
vectorstore = Chroma.from_documents(
documents=chunks,
embedding=embeddings,
persist_directory="./chroma_db"
)
# Persist to disk
vectorstore.persist()
