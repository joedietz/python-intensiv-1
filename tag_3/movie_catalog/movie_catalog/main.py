"""
Startpunkt der Anwendung.
"""

from movie_catalog.models import Movie
from movie_catalog.services import MovieService


def main() -> None:
    """
    Hauptfunktion.
    """
    movies = [
        Movie(
            title="The Matrix",
            year=1999,
            genre="Sci-Fi",
            rating=8.7,
            country="USA",
        ),
        Movie(
            title="Alien",
            year=1979,
            genre="Sci-Fi",
            rating=8.5,
            country="USA",
        ),
        Movie(
            title="Gladiator",
            year=2000,
            genre="Action",
            rating=8.5,
            country="USA",
        ),
        Movie(
            title="Interstellar",
            year=2014,
            genre="Sci-Fi",
            rating=8.7,
            country="USA",
        ),
        Movie(
            title="The Dark Knight",
            year=2008,
            genre="Action",
            rating=9.0,
            country="USA",
        ),
    ]

    service = MovieService(
        movies,
    )

    print("Sci-Fi Filme:")
    print()

    for movie in service.find_by_genre(
        "Sci-Fi",
    ):
        print(movie.title)

    print()
    print("Filme ab 2000:")
    print()

    for movie in service.find_after_year(
        2000,
    ):
        print(movie.title)

    print()
    print("Suche nach 'dark':")
    print()

    for movie in service.search(
        "dark",
    ):
        print(movie.title)

    print()
    print("Top Filme:")
    print()

    for movie in service.top_movies(
        3,
    ):
        print(
            movie.title,
            movie.rating,
        )


if __name__ == "__main__":
    main()
