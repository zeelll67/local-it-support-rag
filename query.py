import chromadb

# 1. Connect to the ChromaDB vault
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="my_document_vault")

# 2. Ask a question (Notice we DON'T use the word "voicemail" or exact keywords!)
question = "What is Jesse Pinkman's phone answer phrase?"

# 3. Search ChromaDB for the top matching chunk
results = collection.query(
    query_texts=[question],
    n_results=1
)

print("\n--- RETRIEVED FROM CHROMADB ---")
print(results["documents"][0][0])
print("-------------------------------\n")