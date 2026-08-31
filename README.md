# JARVIS Work Companion v3

Aplicación local de escritorio inspirada en JARVIS, diseñada como compañero de trabajo para apoyar tareas, estado del sistema y activación por voz. Versión 3 del producto.

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

## Versión comercial v3

La versión v3 está pensada para posicionarse como una solución profesional y comercial, con el siguiente alcance premium:

- UI premium y diseño ejecutivo
- Instalación y empaquetado para distribución
- Soporte técnico y mantenimiento
- Voz más limpia y personalizada
- Autenticación real con biometría opcional
- Modelo de negocio y licencias comerciales
- Documentación profesional para clientes y equipos
- Posibilidad de venta a empresas y organizaciones

### Precio orientativo

Para una oferta comercial más seria y rentable, este producto puede posicionarse en una estructura de precios de empresa:

- $40,000 USD para una versión premium de producto / paquete empresarial
- $10,000 a $20,000 USD para una edición de negocio intermedia
- $1,500 a $5,000 USD para despliegue o licencia de equipo

> Esta estimación refleja una propuesta comercial realista para una versión profesional de producto, no un precio de hobby o prototipo.
