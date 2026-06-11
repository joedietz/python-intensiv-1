"""
Abstract Baseclass: Modul abc

abstractmethod muss von den geerbten Klassen implementiert werden
"""

from abc import ABC, abstractmethod


class Switchable(ABC):
    """Abstrakte Basis Klasse."""

    @abstractmethod
    def turn_on(self): ...

    @abstractmethod
    def turn_off(self): ...

    def stream(self):
        print("...")


class Lightbulb(Switchable):
    """muss turn_on und turn_off implementieren."""

    def turn_on(self):
        print("lb on")

    def turn_off(self):
        print("lb off")


class Fan(Switchable):
    def turn_on(self):
        print("fon")

    def turn_off(self):
        print("f off")


lb = Lightbulb()
f = Fan()

print(isinstance(lb, Switchable))
