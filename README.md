# JARVIS Desktop Assistant

Aplicación local con activación por voz, reconocimiento facial y voz sintética estilo JARVIS.

## Características

- Activa con una frase específica: "jarvis activate"
- Requiere reconocimiento facial para autorizar el arranque
- Voz sintética con TTS tipo JARVIS
- Comandos por voz: status, time, date, report, lock, shutdown
- Interfaz gráfica de escritorio en Python
- Sin necesidad de abrir una página web

## Requisitos

- Python 3.11+
- Cámara para reconocimiento facial
- Micrófono
- macOS / Linux / Windows

## Instalación

```bash
cd /Users/grafica3-7/Desktop/jarvis_automatic
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
python jarvis_desktop.py
```

## Activación

Di esta frase en voz alta:

- "jarvis activate"

Si el sistema reconoce tu rostro, se activa.

## Comandos activos una vez encendido

- "status"
- "time"
- "date"
- "report"
- "lock"
- "shutdown"

## Nota

Este flujo es más realista y orientado a una experiencia tipo asistente personal, sin depender de una página web.
