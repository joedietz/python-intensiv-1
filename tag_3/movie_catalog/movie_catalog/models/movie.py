"""
Filmdatenmodell.
"""

from dataclasses import dataclass


@dataclass
class Movie:
    """
    Repräsentiert einen Film.
    """

    title: str
    year: int
    genre: str
    rating: float
    country: str
