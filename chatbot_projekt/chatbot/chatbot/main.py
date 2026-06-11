# main.py
from chatbot.bot import OpenAiChatBot, ChatBot
import dotenv
import os


def run(chatbot: ChatBot):
    while True:
        prompt = input("Du: ")

        if prompt == "exit":
            print("Good bye ...")
            break

        response = chatbot.talk(prompt)
        print(f"Chatbot: {response}")


def main():
    print("Hello from chatbot!")
    dotenv.load_dotenv()  # setzt Umgebungsvariable SYSTEM_PROMPT
    system_prompt = os.getenv("SYSTEM_PROMPT", "default bot verhalten")
    chatbot = OpenAiChatBot(system_prompt=system_prompt)
    run(chatbot)


if __name__ == "__main__":
    main()
