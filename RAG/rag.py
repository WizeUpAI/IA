from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
# Initialize LLM
llm = ChatOpenAI(temperature=0, model="gpt-4")
# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
llm=llm,
chain_type="stuff",
retriever=compression_retriever,
return_source_documents=True,
chain_type_kwargs={
"prompt": CUSTOM_PROMPT_TEMPLATE
}
)
# Query the system
result = qa_chain({"query": "How do rockets work?"})
print(result["result"])
