from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer


# Define the database URL. Here, we are using MySQL with the pymysql driver.
DATABASE_URL = 'mysql+pymysql://root:admin123@localhost:3306/cinema'

# Create the engine that will communicate with the database
engine = create_engine(DATABASE_URL)

# Declare a base class for our ORM classes
Base = declarative_base()

# Create a session factory, which is used to instantiate sessions
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a session object, which is used to interact with the database
session = Sessionlocal()


# Define the Movies class that maps to the 'movies' table in the database
class Movies(Base):  
    __tablename__ = 'movies'

    # Define columns in the 'movies' table
    title = Column(String(255), primary_key=True)  # title is the primary key
    genre = Column(String(128), nullable=False)   # genre cannot be null
    year = Column(Integer, nullable=False)        # year cannot be null

    # Representation method for displaying movie objects in a readable format
    def __repr__(self):
        return f'Movie(title="{self.title}", genre="{self.genre}", year={self.year})'


# Now, let's explore some of the most common database operations:

# INSERT: Add a new movie to the database
new_movie = Movies(title='Nosferatu', genre='Terror', year=2024)
session.add(new_movie)  # Add the movie object to the session
session.commit()        # Commit the transaction to save it to the database
print(f"Movie '{new_movie.title}' added to the database.")


# SELECT: Query all movies from the database
movies = session.query(Movies).all()  # Fetch all records from the 'movies' table
for movie in movies:
    print(movie)


# DELETE: Delete a movie by its title
# Uncomment the code below to perform a delete operation
# session.query(Movies).filter(Movies.title=='The Batman').delete()
# session.commit()  # Commit the transaction to delete the record
# print("Movie 'The Batman' deleted from the database.")


# UPDATE: Update the genre of a movie
session.query(Movies).filter(Movies.title == 'Nosferatu').update({'genre': 'Terror/Mistery'})
session.commit()  # Commit the changes to the database
print("Movie 'Nosferatu' genre updated to 'Terror/Mistery'.")

# Query the updated movie to verify
updated_movie = session.query(Movies).filter(Movies.title == 'Nosferatu').first()
print(f"Updated Movie: {updated_movie}")


# OPTIONAL: Checking for a movie before updating
# movie_to_update = session.query(Movies).filter(Movies.title == 'Nosferatu').first()
# if movie_to_update:
#     print(f"Movie found: {movie_to_update}")
# else:
#     print("Movie not found.")


# Example of how to filter by multiple conditions (AND)
# This queries for movies of a certain genre and year
filtered_movies = session.query(Movies).filter(Movies.genre == 'Terror/Mystery', Movies.year >= 2020).all()
print("Filtered Movies:")
for movie in filtered_movies:
    print(movie)


# OPTIONAL: Using limit and offset to paginate results
paginated_movies = session.query(Movies).limit(5).offset(0).all()  # Limit to 5 records
print("Paginated Movies:")
for movie in paginated_movies:
    print(movie)


# Finally, always close the session after you're done interacting with the database
session.close()
print("Session closed.")
