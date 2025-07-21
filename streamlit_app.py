import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from agent import loader, embedder, vectorstore, query
from agent.base_agent import run_agent

st.set_page_config(page_title="Marketing KI-Agent", layout="wide")
st.title("🧠 Marketing KI-Agent")

# ========== PDF Upload ==========
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

# ========== Intelligente Agenten-Aufgaben ==========
st.markdown("---")
st.header("🎯 Marketing-Tasks mit KI-Agent")

task = st.selectbox("Wähle eine Aufgabe:", [
    "–",
    "Content Briefing",
    "Wettbewerbsanalyse",
    "SEO Audit",
    "SEO Optimierung",
    "Technisches SEO (Lighthouse)",
    "Kampagnenplanung",
    "Landingpage Strategie",
    "Monatsreport",
    "Marketingmaßnahmen planen"
])

url = st.text_input("🌐 (Optional) Website-URL", placeholder="https://...")

# Dynamische Eingabefelder je nach Modus
if task == "Wettbewerbsanalyse":
    col1, col2 = st.columns(2)
    with col1:
        kunde = st.text_area("👤 Kundentext", height=200)
    with col2:
        mitbewerber = st.text_area("🏢 Mitbewerbertext", height=200)
else:
    context = st.text_area("📄 Kontext oder Text", height=200)

# Button zur Ausführung
if st.button("✅ Absenden"):
    if task == "Content Briefing":
        st.write(run_agent(mode="briefing", text=context))
    elif task == "Wettbewerbsanalyse":
        if kunde and mitbewerber:
            st.write(run_agent(mode="vergleich", text_kunde=kunde, text_mitbewerber=mitbewerber))
        else:
            st.error("❗ Bitte beide Texte ausfüllen.")
    elif task == "SEO Audit":
        st.write(run_agent(mode="seo_audit", text=context))
    elif task == "SEO Optimierung":
        st.write(run_agent(mode="seo_optimize", text=context))
    elif task == "Technisches SEO (Lighthouse)":
        if url:
            st.write(run_agent(mode="seo_lighthouse", url=url))
        else:
            st.error("❗ Bitte eine gültige URL angeben.")
    elif task == "Kampagnenplanung":
        st.write(run_agent(mode="campaign_plan", text=context))
    elif task == "Landingpage Strategie":
        st.write(run_agent(mode="landingpage_strategy", text=context))
    elif task == "Monatsreport":
        st.write(run_agent(mode="monthly_report", text=context))
    elif task == "Marketingmaßnahmen planen":
        st.write(run_agent(mode="tactical_actions", text=context))
