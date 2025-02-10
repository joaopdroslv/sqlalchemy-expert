from infra.configs.connection import DBConnectionHandler
from infra.models.actors import Actors
from infra.models.movies import Movies


class ActorsRepository:
    def select(self):
        """
        Retrieve all actors from the database.
        Returns:
            list: A list of all actors in the database.
        """
        with DBConnectionHandler() as db:
            actors = db.session.query(Actors).all()
            return actors

    def select_with_movie_data(self):
        """
        Selects actor data along with associated movie data from the database.
        This method queries the database to retrieve a list of actors along with
        the titles and genres of the movies they are associated with.
        Returns:
            list: A list of tuples, where each tuple contains the actor's name,
                  the movie title, and the movie genre.
        """
        with DBConnectionHandler() as db:
            data = db.session.query(Actors) \
                .join(Movies, Actors.movie_title == Movies.title) \
                .with_entities(
                    Actors.name,
                    Movies.title,
                    Movies.genre         
                ).all()
            return data
