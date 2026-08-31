import datetime

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
