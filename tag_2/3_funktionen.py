"""
Funktions-Docstrings

- Google Docstring (https://google.github.io/styleguide/pyguide.html)
"""


def database_connect(host: str, password: str) -> None:
    """Baue Verbindung zur Datenbank auf.

    eine Beschreibung wäre hier

    Args:
        host: Der Zielhost
        password: das password

    Returns:
        Database Handle

    Raises:
        ValueError
    """
    pass


print("Docstring anzeigen:", database_connect.__doc__)
