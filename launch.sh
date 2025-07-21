#!/bin/bash

# Optional: Logging für Debug
echo "Starting Streamlit app..."

# Starte nur Streamlit (FastAPI kann später dazukommen)
streamlit run streamlit_app.py --server.port=8000 --server.address=0.0.0.0
