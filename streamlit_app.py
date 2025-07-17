import streamlit as st
from agent import loader, embedder, vectorstore, query

st.set_page_config(page_title="Marketing KI-Agent", layout="wide")

st.title("🧠 Marketing KI-Agent")

uploaded_file = st.file_uploader("📄 Lade eine PDF hoch", type=["pdf"])
question = st.text_input("❓ Deine Frage")

if uploaded_file:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Datei gespeichert!")

    text = loader.load_pdf("uploaded.pdf")
    chunks = []
    for para in text.split("\n\n"):
        if para.strip():
            emb = embedder.create_embedding(para)
            chunks.append({"text": para, "embedding": emb})

    vectorstore.upsert_chunks(chunks)
    st.success(f"✅ {len(chunks)} Chunks gespeichert!")

if question:
    answer = query.query_agent(question)
    st.subheader("📢 GPT-4o Antwort:")
    st.write(answer)
