"""
Methoden

wenn innnerhalb von Klassen auf Klassen referenziert wird, musste vor python 3.13
dieser import ganz oben stattfinden

from __future__ import annotations
"""

from __future__ import annotations


class Logger:
    def __init__(self, level: str = "INFO"):
        self.level = level

    def log(self, message: str) -> None:
        # Instanz-Methode
        print(f"{self.level}: {message}")

    @staticmethod
    def format_string(s: str) -> str:
        return s.upper()

    @classmethod
    def error_logger(cls, s: str) -> Logger:
        obj = cls(level="ERROR")
        return obj


logger = Logger()
# Aufruf der Instanz-Methode log
logger.log(message="Das hat geklappt!")

print("*" * 54)
# via Klassenmethode error_logger neue Instanz erstellen
default_logger = Logger.error_logger(s="")
print(default_logger)
print("*" * 54)

# Aufruf der statischen Methode format_string
upper_string = Logger.format_string(s="hallo")
print(upper_string)
print("*" * 54)
