# Nachmittagsprojekt: Movie Catalog Service

## Tag 2: Filme aus Dateien laden


## Ausgangssituation

Gegeben ist eine CSV-Datei im selben Verzeichnis wie das Python-Programm.

Beispiel:

```csv
title,year,genre,rating,country
The Matrix,1999,Sci-Fi,8.7,USA
Alien,1979,Sci-Fi,8.5,USA
Gladiator,2000,Action,8.4,USA
```

---

## Aufgabe: Projektstruktur aufteilen

Verteile den Code auf mehrere Dateien.

Vorschlag:

```text
movie_catalog/
│
├── main.py
├── movie_loader.py
├── movie_queries.py
└── movies.csv
```

Importiere die Funktionen anschließend in `main.py` und verwende sie dort.
`main.py` ist das Einstiesgsskript, das alle Funktionen aufruft.

---

## Aufgabe: CSV-Dateien laden

### Funktion
In Modul `movie_loader.py`:

`load_movies_from_csv`

### Parameter

* `filename`: Pfad zur CSV-Datei

### Rückgabewert

* Liste von Filmen (dicts)

### Aufgabe

Lade alle Filme aus einer CSV-Datei.
Verwende zum Öffnen der Datei `pathlib.Path`.
Nutze zur Ausgabe der Filme die Funktion `print_movies` aus der vorherigen Übung (Ablegen in `main.py`).

### Beispielaufruf in `main.py`

```python
from pathlib import Path

movies = load_movies_from_csv(
)
print_movies(movies)

```

---

## Aufgabe: Filme als JSON exportieren

### Funktion
In Modul `movie_loader.py`:

`save_movies_to_json`

### Parameter

* `movies`: Liste von Filmen
* `filename`: Name der JSON-Datei

### Rückgabewert

* Kein Rückgabewert

### Aufgabe

Speichere alle Filme in einer JSON-Datei.

### Beispielaufruf in `main.py`

```python
from pathlib import Path

save_movies_to_json(
)
```

---

## Aufgabe: Filme aus JSON laden
In Modul `movie_loader.py`:

### Funktion

`load_movies_from_json`

### Parameter

* `filename`: Pfad zur JSON-Datei

### Rückgabewert

* Liste von Filmen

### Aufgabe

Lade alle Filme aus einer JSON-Datei.

Vergleiche anschließend die Vor- und Nachteile von CSV und JSON.

### Beispielaufruf in `main.py`

```python
from pathlib import Path

movies = load_movies_from_json(
...
)
```

---

## Aufgabe 5: Konfiguration aus TOML

### Funktion
In Modul `movie_loader.py`:

`load_config`

### Parameter

* `filename`: Pfad zur Konfigurationsdatei

### Rückgabewert

* Dictionary mit Konfigurationswerten

### Aufgabe

Erstelle eine TOML- oder YAML-Datei und lade deren Inhalte beim Programmstart.

Beispiel:

```toml
movie_file = "movies.csv"
top_movies_limit = 10
json_export_file = "movies.json"
```

### Beispielaufruf in `main.py`

```python
from pathlib import Path

config = load_config(
    Path(__file__).parent / "config.toml",
)
print(config)
{'movie_file': 'movies.csv', 'top_movies_limit': 10, 'json_export_file': 'movies.json'}
```

---
## Bonus Aufgabe Funktion Sortieren (Ninja Level)

Implementiere eine allgemeine Sortierfunktion im Modul `movie_queries.py`.
Die Sortierung soll über eine übergebene Funktion gesteuert werden.

`sort_movies`

### Parameter

* `movies`: Liste von Filmen
* `key_function`: Funktion zur Sortierung der Filme anhand eines beliebigen Kriteriums (z.B. Jahr, Bewertung, etc.)

### Rückgabewert

* Sortierte Liste von Filmen


### Beispielaufruf in `main.py`

```python
sorted_by_rating = sort_movies(
    movies,
    lambda ??? 
)
```

