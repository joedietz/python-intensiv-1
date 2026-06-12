"""
Logging in Python

Severity Levels:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

- Logger (logger.debug("bla bla"))
- Jeder Logger hat einen oder mehrere Handler
(z.B. StreamHandler, FileHandler, RotatingFilehander)
- Formatter formatiert
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

BASE_DIR = Path(__file__).parent

# einen Logger mit Namen des Moduls erstellen
logger = logging.getLogger(__name__)

# Stream Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

rotating_file_handler = RotatingFileHandler(
    filename=BASE_DIR / "rotating.log",
    maxBytes=300,
    backupCount=3,
    encoding="utf-8",
)
rotating_file_handler.setLevel(logging.INFO)

# Handler hinzufügen
logger.addHandler(stream_handler)
logger.addHandler(rotating_file_handler)

logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
rotating_file_handler.setFormatter(formatter)

logger.debug("DEBUG bla bla")
logger.info("Info Message")
logger.warning("Warning")
logger.error("Error Message")
logger.critical("Critical Message")
