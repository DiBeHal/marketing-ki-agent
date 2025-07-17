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
# 6) Railway erwartet Port 8080 exposed
# --------------------------------------
EXPOSE 8080

# --------------------------------------
# 7) Start-Kommando für FastAPI + Streamlit
# --------------------------------------
CMD ["bash", "launch.sh"]
