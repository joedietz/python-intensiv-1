import pytest

from chatbot.bot import ChatBotError, Role


def test_raise_chatbot_error_if_empty_prompt(chatbot):
    """Erhebe einen Fehler, wenn der User-Prompt leer ist."""
    with pytest.raises(ChatBotError):
        chatbot.talk("   ")


def test_user_message(chatbot):
    chatbot.talk("Hallo")
    assert chatbot.messages[0]["content"] == "Test Bot"
    assert chatbot.messages[1]["content"] == "Hallo"
    assert chatbot.messages[2]["content"] == "Test Anwort"


@pytest.mark.parametrize(
    "index,role,content",
    [
        (0, Role.SYSTEM, "Test Bot"),
        (1, Role.USER, "Muuh"),
        (2, Role.ASSISTANT, "Test Antwort"),
    ],
)
def test_add_prompt(chatbot, index, role, content):
    chatbot.talk("Muuh")
    print("###########", chatbot.messages[index])
    assert chatbot.messages[index]["role"] == role
    assert chatbot.messages[index]["content"] == content
