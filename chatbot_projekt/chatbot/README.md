# Chatbot Projekt

## Abhängigkeiten syncen lokal

    uv sync 

## Abhängigkeiten syncen produktiv
mit no-dev und frozen werden die 
Abhängigkeiten ohne-dev Abhängigkeiten genauso installiert,
wie in der lock-Datei

    uv sync --no-dev --frozen


## Projekt starten

    uv run -m chatbot.main

## Tests ausführen

    uv run -m pytest