from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

load_dotenv('.env')

# Open and read the text file
with open('./docs/Ukraine_text.txt', 'r') as file:
    documents = file.read()

chain = load_qa_chain(llm=OpenAI())
query = 'What is the text about?'
response = chain.invoke({"input_documents": documents, "question": query})
print(response["output_text"])