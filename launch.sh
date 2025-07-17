#!/bin/bash

# 1) Baue dein Docker-Image
docker build -t marketing-ki-agent .

# 2) Starte den Container (interaktiv)
docker run --rm -it --env-file .env marketing-ki-agent
