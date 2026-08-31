import datetime

import jarvis_desktop
from jarvis_core import JarvisCore


def test_status_report_contains_online_system():
    jarvis = JarvisCore()
    status = jarvis.get_status_summary()

    assert status["name"] == "JARVIS"
    assert status["status"] == "online"
    assert "uptime" in status["system"]


def test_uptime_is_not_zero():
    jarvis = JarvisCore()
    uptime = jarvis.get_system_info()["uptime"]

    assert "0:00:00" not in uptime
    assert isinstance(uptime, str)


def test_check_face_reports_missing_opencv_face_support(monkeypatch):
    app = object.__new__(jarvis_desktop.JarvisDesktopApp)
    captured = []
    app.log = lambda text: captured.append(text)

    class DummyData:
        haarcascades = "/tmp/"

    class DummyCv2:
        data = DummyData()

    monkeypatch.setattr(jarvis_desktop, "cv2", DummyCv2)

    result = app.check_face()

    assert result is False
    assert any("OpenCV face detection is unavailable" in message for message in captured)
