### Aufgabe: Ampel-Zustände mit Enum und Klasse

Wir modellieren eine Ampel mit drei Zuständen: **ROT**,  **GELB** und **GRÜN**.
RED → GREEN → YELLOW → RED.

#### Teil 1: Enum erstellen

* Erstelle eine Enumeration `TrafficLightState` mit den Zuständen:

  * `RED`
  * `YELLOW`
  * `GREEN`

#### Teil 2: Klasse implementieren

Erstelle eine Klasse `TrafficLight`:

* Beim Erzeugen (`__init__`) soll der Anfangszustand **ROT** sein.
* Implementiere die Methode `next_state()`:

  * Übergang erfolgt in dieser Reihenfolge:
    **ROT → GRÜN → GELB → ROT**
* Die Methode `__str__()` soll den aktuellen Zustand als Text zurückgeben.

#### Teil 3: Testen

* Erzeuge ein Objekt der Klasse.
* Gib den Anfangszustand aus.
* Rufe mehrmals `next_state()` auf und gib jeweils den neuen Zustand aus.

