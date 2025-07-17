# --------------------------------------
# 1) Basis-Image
# --------------------------------------
FROM python:3.11-slim

# --------------------------------------
# 2) Arbeitsverzeichnis
# --------------------------------------
WORKDIR /app

# --------------------------------------
# 3) System-Updates & System-Abhängigkeiten
# --------------------------------------
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# --------------------------------------
# 4) Projektdateien kopieren
# --------------------------------------
COPY . /app

# --------------------------------------
# 5) Python-Abhängigkeiten installieren
# --------------------------------------
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------
# 6) .env über docker-compose.yml laden
# Kein COPY hier nötig!
# --------------------------------------

# --------------------------------------
# 7) Start-Kommando
# --------------------------------------

# === Option A: main.py testen ===
# CMD ["python", "main.py"]

# === Option B: FastAPI starten ===
CMD ["uvicorn", "agent.api:app", "--host", "0.0.0.0", "--port", "8000"]

# === Option C: Streamlit starten ===
# CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "8000", "--server.address", "0.0.0.0"]
