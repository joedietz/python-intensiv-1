"""
Schema der Excpetions
Exception Hierachy: https://docs.python.org/3/library/exceptions.html

try:
    .... happy path, zero cost
except  <EXCEPTION>:

finally:
    wird immer ausgeführt
else:
    wird immer ausgeführt, wenn KEINE Exception

"""

import requests


class ApiError(Exception): ...


def show_temp(latitude: float, longitude: float):
    """Zeige Temperaturen an.

    Raises:
        ApiError (wenn was schiefging)
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m"
    )
    try:
        result = requests.get(url, timeout=10)
        result.raise_for_status()  # raise ValueErrro
    except requests.exceptions.RequestException as e:
        print(f"Fehler ist aufgetreten: {e}")
        raise ApiError("Fehler in der Api")
    else:
        data = result.json()
        print(data)


show_temp(latitude=52.53, longitude=13.41)
show_temp(latitude=52.53, longitude=3434334.3434)

####################
d = {"b": 3}

# Versuchen, auf Key b zuzugreifen
try:
    d["b"]
except KeyError as e:
    print("Key ist nicht drin")
    # um die Ursprungs Exception nicht zu verlieren
    raise

# 2. Möglichkeit: ERst prüfen, ob b im Dict
if "b" in d:
    print("b ist drin")
else:
    print("b ist nicht drin")
