import csv
import chromadb

# 1. Connect to your local ChromaDB directory
client = chromadb.PersistentClient(path="./my_chroma_db")

# 2. Delete the old collection so timestamp-only data is wiped clean
try:
    client.delete_collection(name="my_document_vault")
except Exception:
    pass

collection = client.get_or_create_collection(name="my_document_vault")

# 3. Read all columns dynamically from your CSV
csv_file_path = "synthetic_it_support_tickets.csv"
documents = []

with open(csv_file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Detected CSV columns:", reader.fieldnames)

    for i, row in enumerate(reader):
        # Combine every column and its text into a clean, readable record
        row_text = " | ".join([f"{col}: {val}" for col, val in row.items() if val])
        documents.append(row_text)

        if i >= 500:
            break

# 4. Store in ChromaDB
doc_ids = [f"ticket_{i}" for i in range(len(documents))]
collection.add(documents=documents, ids=doc_ids)

print(f"\nSUCCESS! Ingested {len(documents)} complete IT support tickets.\n")