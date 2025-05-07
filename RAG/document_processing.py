import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Load documents
loader = DirectoryLoader('./documents/', glob="**/*.pdf")
documents = loader.load()
# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
chunk_size=1000,
chunk_overlap=200,
length_function=len,
)
chunks = text_splitter.split_documents(documents)
