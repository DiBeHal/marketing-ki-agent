#!/bin/bash

# Starte FastAPI im Hintergrund
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Starte Streamlit im Vordergrund auf Port 8080 (wichtig für Railway)
streamlit run streamlit_app.py --server.port=8080 --server.enableCORS=false
