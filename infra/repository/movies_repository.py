from infra.configs.connection import DBConnectionHandler
from infra.models.movies import Movies

from sqlalchemy.orm.exc import NoResultFound


class MoviesRepository:
    def select(self):
        """
        Retrieve all movies from the database.
        Returns:
            list: A list of all movies in the database.
        """
        with DBConnectionHandler() as db:
            movies = db.session.query(Movies).all()
            return movies

    def force_error(self):
        with DBConnectionHandler() as db:
            try:
                movie = db.session.query(Movies).filter(Movies.genre=='Unkown').one()
                return movie
            # We can customize the error handling behavior for specific cases here
            except NoResultFound:
                return []
                # or
                # return 'No movies found!'
                # db.session.rollback()  # If needed

    def insert(self, title, genre, year):
        """
        Inserts a new movie record into the database.
        Args:
            title (str): The title of the movie.
            genre (str): The genre of the movie.
            year (int): The release year of the movie.
        Returns:
            db_movie (Movies): The movie object that was inserted into the database.
        """
        with DBConnectionHandler() as db:
            db_movie = Movies(title=title, genre=genre, year=year)
            db.session.add(db_movie)
            db.session.commit()
            return db_movie

    def update(self, title, **kwargs):
        """
        Update the attributes of a movie record in the database.
        Args:
            title (str): The title of the movie to be updated.
            **kwargs: Arbitrary keyword arguments representing 
                        the attributes to be updated and their new values.
        Returns:
            None
        """
        with DBConnectionHandler() as db:
            db_movie = db.session.query(Movies).filter(Movies.title==title).first()
            for key, value in kwargs.items():
                setattr(db_movie, key, value)
            db.session.commit()

    def delete(self, title):
        """
        Deletes a movie record from the database based on the given title.
        Args:
            title (str): The title of the movie to be deleted.
        """
        with DBConnectionHandler() as db:
            db.session.query(Movies).filter(Movies.title==title).delete()
            db.session.commit()
