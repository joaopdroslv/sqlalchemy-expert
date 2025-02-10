from infra.configs.base import Base
from infra.models.movies import Movies
from infra.models.actors import Actors

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="function")
def test_db():
    """Creates an in-memory SQLite database and populates it with 10 records."""

    # Creating a temporary in-memory database
    TEST_DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Creating the tables in the test database
    Base.metadata.create_all(bind=engine)

    # Creating a session to manipulate the data
    session = TestingSessionLocal()

    # Inserting 30 records into the database
    movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994},
        {"title": "The Dark Knight", "genre": "Action", "year": 2008},
        {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
        {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
        {"title": "The Godfather", "genre": "Crime", "year": 1972},
        {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999},
        {"title": "Gladiator", "genre": "Action", "year": 2000},
        {"title": "Forrest Gump", "genre": "Drama", "year": 1994},
        {"title": "The Lion King", "genre": "Animation", "year": 1994},
        {"title": "Star Wars: A New Hope", "genre": "Sci-Fi", "year": 1977},
    ]
    db_movies = [Movies(**movie) for movie in movies]
    session.bulk_save_objects(db_movies)  # Inserting in an optimized way
    session.commit()

    yield session  # Returns the session for the tests to use

    # Closing session and deleting the database at the end of the tests
    session.close()
    engine.dispose()


def test_select_movies(test_db):
    movies = test_db.query(Movies).all()
    assert len(movies) == 10
