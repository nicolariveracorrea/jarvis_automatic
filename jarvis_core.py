import datetime
import os
import platform
import socket
import shutil
from typing import Dict, Any


class JarvisCore:
    def __init__(self):
        self.name = "JARVIS"
        self.version = "1.2.0"
        self.start_time = datetime.datetime.now()
        self.api_keys = {
            "openai": os.environ.get("OPENAI_API_KEY"),
            "weather": os.environ.get("WEATHER_API_KEY"),
        }

    def get_system_info(self) -> Dict[str, Any]:
        uname = platform.uname()
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return {
            "hostname": hostname,
            "ip": ip_address,
            "platform": platform.platform(),
            "system": uname.system,
            "release": uname.release,
            "machine": uname.machine,
            "processor": uname.processor,
            "python_version": platform.python_version(),
            "uptime": self._format_uptime(),
        }

    def get_resources(self) -> Dict[str, Any]:
        disk = shutil.disk_usage("/")
        total, used, free = disk.total, disk.used, disk.free
        return {
            "disk_total": self._format_bytes(total),
            "disk_used": self._format_bytes(used),
            "disk_free": self._format_bytes(free),
            "disk_percent": round((used / total) * 100, 1),
        }

    def get_status_summary(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": "online",
            "version": self.version,
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "date": datetime.datetime.now().strftime("%A, %d %B %Y"),
            "system": self.get_system_info(),
            "resources": self.get_resources(),
        }

    def handle_command(self, command: str) -> Dict[str, Any]:
        text = (command or "").strip()
        if not text:
            return {
                "reply": "No command received.",
                "voice": "No command received.",
                "status": "idle",
            }

        normalized = text.lower()

        if any(keyword in normalized for keyword in ["hello", "hi", "hey", "hola"]):
            return self._build_response(
                "Hello, sir. JARVIS online and ready to assist.",
                "Hello, sir. JARVIS online and ready to assist.",
                intent="greeting",
            )

        if any(keyword in normalized for keyword in ["status", "state", "system", "diagnostic", "diagnostico"]):
            status = self.get_status_summary()
            return self._build_response(
                f"System status nominal. Time {status['time']}. Uptime {status['system']['uptime']}.",
                f"System status nominal. Time {status['time']}. Uptime {status['system']['uptime']}.",
                extra=status,
                intent="status",
            )

        if any(keyword in normalized for keyword in ["time", "hora"]):
            current = datetime.datetime.now().strftime("%I:%M %p")
            return self._build_response(f"The current time is {current}.", f"The current time is {current}.", intent="time")

        if any(keyword in normalized for keyword in ["date", "fecha"]):
            current = datetime.datetime.now().strftime("%A, %d %B %Y")
            return self._build_response(f"Today is {current}.", f"Today is {current}.", intent="date")

        if any(keyword in normalized for keyword in ["report", "summary", "reporte", "resumen"]):
            summary = self.get_status_summary()
            return self._build_response(
                f"Daily status report: system online, workload stable, disk usage at {summary['resources']['disk_percent']} percent.",
                f"Daily status report: system online, workload stable, disk usage at {summary['resources']['disk_percent']} percent.",
                extra=summary,
                intent="report",
            )

        if any(keyword in normalized for keyword in ["weather", "clima", "temperatura"]):
            return self._build_response(
                "Weather integration is ready. Add your API key to enable live weather data.",
                "Weather integration is ready. Add your API key to enable live weather data.",
                intent="weather",
            )

        if any(keyword in normalized for keyword in ["news", "noticias", "headline"]):
            return self._build_response(
                "News feed ready. Connect an external API to stream headlines and updates.",
                "News feed ready. Connect an external API to stream headlines and updates.",
                intent="news",
            )

        if any(keyword in normalized for keyword in ["open", "abrir", "launch"]):
            return self._build_response(
                "I can prepare local actions and external integrations. Tell me which app or service you want to open.",
                "I can prepare local actions and external integrations. Tell me which app or service you want to open.",
                intent="open",
            )

        if any(keyword in normalized for keyword in ["shutdown", "power off", "apagar"]):
            return self._build_response(
                "I cannot power down the host from here, sir. I can prepare the shutdown sequence if you authorize it.",
                "I cannot power down the host from here, sir. I can prepare the shutdown sequence if you authorize it.",
                intent="shutdown",
            )

        return self._build_response(
            "I am ready to assist. Ask for status, diagnostics, time, date, or system summary.",
            "I am ready to assist. Ask for status, diagnostics, time, date, or system summary.",
            intent="default",
        )

    def _build_response(self, reply: str, voice: str, extra: Dict[str, Any] = None, intent: str = "default") -> Dict[str, Any]:
        response = {
            "reply": reply,
            "voice": voice,
            "status": "online",
            "intent": intent,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        if extra:
            response["extra"] = extra
        return response

    def speak(self, text: str) -> Dict[str, Any]:
        try:
            import pyttsx3

            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            return {"success": True, "message": "Voice output started."}
        except Exception as exc:  # pragma: no cover - optional dependency
            return {"success": False, "message": f"Voice unavailable: {exc}"}

    @staticmethod
    def _format_bytes(value: int) -> str:
        units = ["B", "KB", "MB", "GB", "TB"]
        size = float(value)
        unit_index = 0
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1
        return f"{size:.2f} {units[unit_index]}"

    def _format_uptime(self) -> str:
        elapsed = datetime.datetime.now() - self.start_time
        total_seconds = max(int(elapsed.total_seconds()), 1)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
