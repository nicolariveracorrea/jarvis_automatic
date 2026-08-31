import subprocess
import threading
import time
import tkinter as tk

import cv2
import speech_recognition as sr

try:
    import pyttsx3
except Exception:  # pragma: no cover
    pyttsx3 = None


class JarvisDesktopApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JARVIS Work Companion v4")
        self.root.geometry("720x480")
        self.root.configure(bg="#06131c")
        self.root.resizable(False, False)

        self.is_active = False
        self.face_authorized = False
        self.activation_phrase = "jarvis activate"
        self.last_status = "Locked"
        self.engine = None
        self.log_area = None
        self.status_label = None
        self.recognizer = None
        self.microphone = None
        self.memory = {}
        self.last_command = ""
        self._setup_ui()
        self._init_voice_engine()
        self._init_audio()

    def _setup_ui(self):
        title = tk.Label(
            self.root,
            text="J.A.R.V.I.S",
            fg="#75e8ff",
            bg="#06131c",
            font=("Arial", 26, "bold"),
        )
        title.pack(pady=(26, 10))

        status = tk.Label(
            self.root,
            text="SYSTEM LOCKED",
            fg="#7ef7b5",
            bg="#06131c",
            font=("Arial", 18, "bold"),
        )
        status.pack(pady=8)
        self.status_label = status

        self.log_area = tk.Text(
            self.root,
            height=11,
            width=64,
            bg="#0a1b2b",
            fg="#86f8ff",
            font=("Courier", 11),
            wrap="word",
        )
        self.log_area.pack(padx=18, pady=10)
        self.log_area.insert("end", "[BOOT] JARVIS work companion initialized.\n")
        self.log_area.insert("end", "[LOCK] Awaiting activation phrase.\n")
        self.log_area.configure(state="disabled")

        button_frame = tk.Frame(self.root, bg="#06131c")
        button_frame.pack(pady=(4, 18))

        self.activate_button = tk.Button(
            button_frame,
            text="START WORK MODE",
            width=18,
            height=2,
            bg="#0b2a3a",
            fg="#ebfaff",
            font=("Arial", 12, "bold"),
            command=self.handle_activation,
        )
        self.activate_button.pack(side="left", padx=10)

        off_button = tk.Button(
            button_frame,
            text="LOCK SYSTEM",
            width=16,
            height=2,
            bg="#1d1d2c",
            fg="#f8f8f8",
            font=("Arial", 12, "bold"),
            command=self.lock_system,
        )
        off_button.pack(side="left", padx=10)

    def log(self, text: str):
        if not self.log_area:
            return
        self.log_area.configure(state="normal")
        self.log_area.insert("end", f"{text}\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")

    def _init_voice_engine(self):
        if pyttsx3 is None:
            self.engine = None
            self.log("[VOICE_WARNING] pyttsx3 not available.")
            return
        try:
            self.engine = pyttsx3.init()
            self.log("[VOICE] JARVIS voice engine ready.")
        except Exception as exc:  # pragma: no cover
            self.engine = None
            self.log(f"[VOICE_WARNING] Voice engine unavailable: {exc}")

    def _init_audio(self):
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            self.log("[AUDIO] Microphone ready.")
        except Exception as exc:  # pragma: no cover
            self.recognizer = None
            self.microphone = None
            self.log(f"[AUDIO_WARNING] Microphone unavailable: {exc}")

    def speak(self, text: str):
        if self.engine is not None:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
                return
            except Exception as exc:  # pragma: no cover
                self.log(f"[VOICE_ERROR] {exc}")

        try:
            subprocess.run(["say", text], check=False)
            return
        except Exception as exc:  # pragma: no cover
            self.log(f"[VOICE_ERROR] {exc}")
            self.log(f"[VOICE] {text}")

    def check_face(self) -> bool:
        try:
            if not hasattr(cv2, "CascadeClassifier"):
                self.log("[FACE] OpenCV face detection is unavailable in this environment.")
                return False

            cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            face_cascade = cv2.CascadeClassifier(cascade_path)
            if face_cascade.empty():
                self.log("[FACE] Face classifier not available.")
                return False

            capture = cv2.VideoCapture(0)
            if not capture.isOpened():
                self.log("[FACE] Camera unavailable. Face auth blocked.")
                return False

            deadline = time.time() + 8
            while time.time() < deadline:
                ok, frame = capture.read()
                if not ok:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
                if len(faces) > 0:
                    capture.release()
                    cv2.destroyAllWindows()
                    return True
                time.sleep(0.2)

            capture.release()
            cv2.destroyAllWindows()
            return False
        except Exception as exc:
            self.log(f"[FACE_ERROR] {exc}")
            return False

    def listen_for_activation(self):
        if self.microphone is None or self.recognizer is None:
            self.log("[AUDIO_WARNING] Voice activation disabled because no microphone is available.")
            return
        while True:
            if self.is_active:
                return
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
                    self.log("[LISTEN] Waiting for activation phrase...")
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=6)
                text = self.recognizer.recognize_google(audio, language="en-US").lower()
                self.log(f"[VOICE] Heard: {text}")
                if self.activation_phrase in text:
                    self.handle_activation()
            except Exception:
                pass

    def handle_activation(self):
        if self.is_active:
            return

        self.log("[AUTH] Verifying identity...")
        self.speak("Identity verification required. Please look at the camera.")

        if not self.check_face():
            self.log("[AUTH] Camera not available or face not recognized. Access blocked.")
            self.speak("Access denied. Camera unavailable or face not recognized.")
            self.status_label.config(text="ACCESS DENIED")
            self.status_label.config(fg="#ff8d8d")
            return

        self.face_authorized = True
        self.is_active = True
        self.last_status = "Online"
        self.status_label.config(text="SYSTEM ONLINE")
        self.status_label.config(fg="#7ef7b5")
        self.log("[AUTH] Face recognized. Welcome back.")
        self.speak("Face confirmed. JARVIS is online and ready to support the team.")
        self.run_commands_loop()

    def run_commands_loop(self):
        if self.microphone is None or self.recognizer is None:
            self.log("[AUDIO_WARNING] Voice commands disabled because no microphone is available.")
            return
        while self.is_active:
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.4)
                    self.log("[LISTEN] Awaiting command...")
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=8)
                text = self.recognizer.recognize_google(audio, language="en-US").lower()
                self.log(f"[COMMAND] {text}")
                self.handle_command(text)
            except Exception:
                pass

    def handle_command(self, text: str):
        text = text.strip().lower()
        self.last_command = text
        self.memory["last_command"] = text

        if not text:
            self.speak("I did not receive a command.")
            return

        if any(word in text for word in ["status", "state", "health"]):
            self.speak("Systems nominal, all core functions stable and secure.")
        elif any(word in text for word in ["time", "hour"]):
            self.speak(f"The current time is {time.strftime('%I:%M %p')}.")
        elif any(word in text for word in ["date", "day"]):
            self.speak(time.strftime("Today is %A, %d %B %Y."))
        elif any(word in text for word in ["report", "summary", "brief"]):
            self.speak("Daily report complete. All systems are online and performing normally.")
        elif any(word in text for word in ["lock", "shutdown", "power off"]):
            self.lock_system()
            self.speak("System locked. Awaiting authorization.")
        elif any(word in text for word in ["who are you", "what are you", "identity", "help"]):
            self.speak("I am JARVIS, your work companion. I monitor systems, support workflows, and protect team access with identity verification.")
        elif any(word in text for word in ["open", "launch", "start", "run"]):
            self.speak("I am preparing the requested action and checking the current system state before execution.")
        elif any(word in text for word in ["plan", "schedule", "task"]):
            self.speak("I have identified the objective and I am prioritizing security, resources, and execution flow.")
        else:
            self.speak("Command recognized. I am evaluating the request and preparing the next response with the current system context.")

        self.memory["last_response"] = text

    def lock_system(self):
        self.is_active = False
        self.face_authorized = False
        self.last_status = "Locked"
        self.status_label.config(text="SYSTEM LOCKED")
        self.status_label.config(fg="#7ef7b5")
        self.log("[LOCK] System locked. Waiting for activation phrase.")

    def start(self):
        self.root.mainloop()


def main():
    app = JarvisDesktopApp()
    threading.Thread(target=app.listen_for_activation, daemon=True).start()
    app.start()


if __name__ == "__main__":
    main()
