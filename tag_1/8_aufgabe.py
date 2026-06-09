"""
Schreibe eine Funktion get_hot_work_days, die aus einer Liste von Dictionaries
(weekday_temperatures) alle heißen Arbeitstage ermittelt.

Jeder Eintrag enthält die Schlüssel day, date und temperature.

Wochenendtage sind in WEEKEND definiert und sollen nicht berücksichtigt werden.
Zusätzlich soll nur nach Tagen gefiltert werden, deren Temperatur größer oder
gleich einem übergebenen Grenzwert min_temp ist. Die Funktion soll eine Liste
von Tupeln zurückgeben, die jeweils aus dem Datum und der Temperatur bestehen.

Beispiel: get_hot_work_days(weekday_temperatures, 30)
liefert
[('2019-07-15', 31), ('2019-07-16', 33), ('2019-07-23', 31)].
"""

MIN_TEMPERATURE = 30
WEEKEND = ("Saturday", "Sunday")


weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]


def get_hot_work_days(temperatures: list[dict], temperatur: int) -> list[tuple]:
    warm_days = []
    for temp in temperatures:
        if temp["day"] not in WEEKEND and temp["temperature"] >= temperatur:
            warm_days.append(
                (temp["date"], temp["temperature"]),
            )
    return warm_days


result = get_hot_work_days(weekday_temperatures, MIN_TEMPERATURE)
print(result)
