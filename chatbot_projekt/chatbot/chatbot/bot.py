"""
chatbot/bot.py
Chatbot Klasse

3. Rollen (
User => der mensch,
Assistant => die Antwort des LLMs
System => das Verhalten des Bots
"""

import openai
from enum import StrEnum
from typing import Protocol


class ChatBotError(Exception):
    pass


class Role(StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"


class ChatBot(Protocol):
    """Interface für alle Chatbots."""

    def talk(self, prompt: str) -> str: ...


class DummyChatBot:
    def talk(self, prompt: str) -> str:
        return prompt.upper()


class OpenAiChatBot:
    def __init__(self, model: str = "gpt-4o-mini", system_prompt: str = "default"):
        self.model = model
        self.system_prompt = system_prompt
        self.client = openai.OpenAI()
        self.messages: list[dict] = []
        self._add_system_prompt()

    def _add_system_prompt(self) -> None:
        self.messages.append(
            {
                "role": Role.SYSTEM,
                "content": self.system_prompt,
            }
        )

    def _call_chatbot(self) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,  # type: ignore
            )
            content = response.choices[0].message.content
        except openai.APIError as e:
            raise ChatBotError(f"in der Api ist ein Fehler aufgetreten: {e}")

        return content or ""

    def talk(self, prompt: str) -> str:
        if not prompt.strip():
            raise ChatBotError("Der Prompt darf nicht leer sein!")

        self.messages.append(
            {
                "role": Role.USER,
                "content": prompt,
            }
        )
        content = self._call_chatbot()

        self.messages.append(
            {
                "role": Role.ASSISTANT,
                "content": content,
            }
        )

        return content
