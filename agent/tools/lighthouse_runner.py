import subprocess
import json
import os

def run_lighthouse(url: str, output_path="report.json") -> dict:
    """
    Führt Lighthouse aus und liefert das Ergebnis als Dict zurück.
    """
    script_path = os.path.join(os.getcwd(), "tools", "run_lighthouse.mjs")
    try:
        subprocess.run(["node", script_path, url, output_path], check=True)
        with open(output_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Lighthouse-Fehler: {e}")
