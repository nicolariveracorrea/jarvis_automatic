# JARVIS Work Companion

Aplicación local de escritorio inspirada en JARVIS, diseñada como compañero de trabajo para apoyar tareas, estado del sistema y activación por voz.

## Características

- Activación por voz con la frase: "jarvis activate"
- Interfaz gráfica de escritorio en Python con Tkinter
- Verificación de identidad por rostro cuando hay cámara disponible
- Voz sintética con fallback nativo del sistema
- Comandos por voz básicos: status, time, date, report, lock, shutdown
- Modo seguro si no hay cámara, micrófono o soporte facial completo disponible

## Requisitos

- Python 3.9+
- Micrófono para activación por voz
- Cámara opcional para reconocimiento facial
- Sistema operativo compatible con Tkinter y voz del sistema

## Instalación

```bash
cd /Users/grafica3-7/Desktop/jarvis_automatic
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
cd /Users/grafica3-7/Desktop/jarvis_automatic
source .venv/bin/activate
python jarvis_desktop.py
```

## Activación

Di esta frase en voz alta:

- "jarvis activate"

Si la cámara está disponible y el entorno lo soporta, el sistema intenta verificar el rostro antes de activar el modo de trabajo.

## Comandos activos una vez encendido

- "status"
- "time"
- "date"
- "report"
- "lock"
- "shutdown"

## Nota importante

Este proyecto está pensado como compañero de trabajo de escritorio, no como asistente personal doméstico. En entornos sin cámara o sin soporte completo de OpenCV, la app sigue ejecutándose en modo seguro en vez de romperse.
