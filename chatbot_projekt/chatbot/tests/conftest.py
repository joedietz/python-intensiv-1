import pytest

from chatbot.bot import OpenAiChatBot


@pytest.fixture
def chatbot(monkeypatch):
    # für die Laufzeit des Tests setzen wir die Umgebungsvaqriable
    # des Openai SDK auf dummyvalue
    monkeypatch.setenv("OPENAI_API_KEY", "dummyvalue")
    chatbot = OpenAiChatBot(system_prompt="Test Bot")

    # wenn im Test talk() -> _call_chatbot() aufruft, wir das hier aufgerufen:
    chatbot._call_chatbot = lambda: "Test Anwort"
    return chatbot
