"""
Geschäftslogik für Filme.
"""

from movie_catalog.models import Movie


class MovieService:
    """
    Verwaltet eine Liste von Filmen.
    """

    def __init__(
        self,
        movies: list[Movie],
    ) -> None:
        """
        Initialisiert den Service.
        """
        self.movies = movies

    def find_by_genre(
        self,
        genre: str,
    ) -> list[Movie]:
        """
        Sucht Filme eines Genres.
        """
        result: list[Movie] = []

        for movie in self.movies:
            if movie.genre == genre:
                result.append(movie)

        return result

    def find_after_year(
        self,
        year: int,
    ) -> list[Movie]:
        """
        Sucht Filme ab einem Jahr.
        """
        result: list[Movie] = []

        for movie in self.movies:
            if movie.year >= year:
                result.append(movie)

        return result

    def search(
        self,
        search_term: str,
    ) -> list[Movie]:
        """
        Durchsucht Filmtitel.
        """
        result: list[Movie] = []

        search_term = search_term.lower()

        for movie in self.movies:
            if search_term in movie.title.lower():
                result.append(movie)

        return result

    def top_movies(
        self,
        limit: int,
    ) -> list[Movie]:
        """
        Liefert die bestbewerteten Filme.
        """
        sorted_movies = sorted(
            self.movies,
            key=lambda movie: movie.rating,
            reverse=True,
        )

        return sorted_movies[:limit]
