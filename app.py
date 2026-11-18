import streamlit as st
import chromadb
import ollama

# Set up the web page layout
st.set_page_config(page_title="Local IT Support RAG", page_icon="🔒")
st.title("🔒 Local IT Support Intelligence Assistant")
st.write("Query and summarize 500+ IT support tickets completely offline.")

# 1. Connect to your existing ChromaDB database
client = chromadb.PersistentClient(path="./my_chroma_db")
try:
    collection = client.get_collection(name="my_document_vault")
except Exception as e:
    st.error("Collection not found! Please run your ingest.py script first.")

# 2. Create a text box for user input
question = st.text_input("What would you like to know?", placeholder="e.g., Summarize the common login or network issues.")

if question:
    with st.spinner("Searching 500+ tickets and generating local insights..."):
        
        # 3. Retrieve the TOP 10 matching tickets from ChromaDB (instead of just 1!)
        results = collection.query(
            query_texts=[question],
            n_results=10
        )
        
        # Combine all 10 retrieved tickets into one readable block for the LLM
        retrieved_tickets = results["documents"][0]
        retrieved_context = "\n".join([f"- {ticket}" for ticket in retrieved_tickets])

        # 4. Construct the prompt for Ollama
        prompt = f"""
        You are an IT Support Data Analyst. Use ONLY the provided support ticket records below to answer the user's question. Summarize patterns clearly.
        
        Retrieved Support Tickets:
        {retrieved_context}
        
        Question:
        {question}
        """

        # 5. Send prompt to local Llama 3.2 model via Ollama
        response = ollama.chat(
            model='llama3.2:3b',
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = response['message']['content']

        # 6. Display the Answer nicely in the UI
        st.success("Analysis Complete!")
        st.subheader("Answer:")
        st.write(answer)

        # 7. Show all 10 source tickets pulled from ChromaDB
        with st.expander("🔍 View Retrieved Support Tickets (Top 10 Matches)"):
            st.text(retrieved_context)