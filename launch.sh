#!/bin/bash

# Starte FastAPI im Hintergrund auf Port 8000
uvicorn agent.api:app --host 0.0.0.0 --port 8000 &

# Starte Streamlit im Vordergrund auf Port 8080 (für Railway sichtbar)
streamlit run streamlit_app.py --server.port 8080 --server.address 0.0.0.0
