# JARVIS Work Companion v3

Aplicación local de escritorio inspirada en la idea de un asistente ejecutivo inteligente, diseñada como compañero de trabajo para monitorear sistemas, responder comandos por voz, verificar identidad y apoyar productividad en tiempo real. Versión 3 del producto.

## Visión

JARVIS Work Companion v3 busca funcionar como una capa inteligente de ejecución para entornos de trabajo: asistencia por voz, monitoreo del sistema, autenticación de usuario y control operativo sin depender de una página web ni de un navegador.

## Stack tecnológico

- Python 3.9+
- Tkinter para interfaz gráfica de escritorio
- OpenCV para procesamiento visual y reconocimiento facial
- SpeechRecognition para reconocimiento de voz
- pyttsx3 para síntesis de voz
- Flask para API opcional y módulos HTTP
- Git y GitHub para versionado y despliegue de código
- pytest para validación automática
- macOS native voice fallback mediante `say`

## Capacidades actuales

- Activación por voz con la frase: "jarvis activate"
- Interfaz gráfica de escritorio moderna y ejecutable localmente
- Verificación de identidad por rostro cuando hay cámara disponible
- Voz sintética con soporte nativo del sistema como fallback
- Comandos por voz básicos: status, time, date, report, lock, shutdown
- Modo seguro si no hay cámara, micrófono o soporte facial completo disponible
- Validación y monitoreo del estado del sistema
- Estructura lista para expansión con automatización y control de flujo de trabajo

## Requisitos

- Python 3.9+
- Micrófono para activación por voz
- Cámara opcional para reconocimiento facial
- Sistema operativo compatible con Tkinter y voz del sistema
- Entorno con OpenCV funcional para autenticación visual real

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

## Arquitectura del proyecto

- `jarvis_core.py`: lógica central del asistente, comandos, estado del sistema y respuestas
- `jarvis_desktop.py`: interfaz de escritorio, voz, autenticación y flujo principal
- `app.py`: versión web/HTTP opcional basada en Flask
- `tests/test_jarvis_core.py`: validación automatizada
- `start_jarvis.sh`: lanzador rápido del proyecto

## Modo seguro y robustez

El sistema está preparado para manejar escenarios reales donde no hay cámara, no hay micrófono o el entorno no ofrece soporte completo para OpenCV. En esos casos la aplicación no se rompe, sino que corre en modo seguro y mantiene estabilidad.

## Nota importante

Este proyecto está pensado como compañero de trabajo de escritorio, no como asistente personal doméstico. La lógica está orientada a productividad, soporte operativo y ejecución inteligente en entornos profesionales.

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

## Roadmap técnico

Futuras ampliaciones recomendadas para llevar la v3 a nivel producto comercial:

- autenticación biométrica con mejor hardware real
- integración con APIs de clima, email, calendario y gestión de tareas
- voz mejorada con TTS premium y modelos más naturales
- sistema de plugins y módulos empresariales
- empaquetado para Windows, macOS y Linux
- módulo de seguridad y auditoría para uso empresarial
- control remoto y despliegue en equipos internos
