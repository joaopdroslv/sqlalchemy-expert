CREATE DATABASE IF NOT EXISTS cinema;

USE cinema;

CREATE TABLE IF NOT EXISTS movies (
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(128) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (title)
);

CREATE TABLE IF NOT EXISTS actors (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    movie_title VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (movie_title) REFERENCES movies(title)
)

-- Inserting data into the 'movies' table
INSERT INTO movies (title, genre, year) VALUES ('The Shawshank Redemption', 'Drama', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Dark Knight', 'Action', 2008);
INSERT INTO movies (title, genre, year) VALUES ('Inception', 'Sci-Fi', 2010);
INSERT INTO movies (title, genre, year) VALUES ('Pulp Fiction', 'Crime', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Godfather', 'Crime', 1972);
INSERT INTO movies (title, genre, year) VALUES ('The Matrix', 'Sci-Fi', 1999);
INSERT INTO movies (title, genre, year) VALUES ('Gladiator', 'Action', 2000);
INSERT INTO movies (title, genre, year) VALUES ('Forrest Gump', 'Drama', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Lion King', 'Animation', 1994);
INSERT INTO movies (title, genre, year) VALUES ('Star Wars: A New Hope', 'Sci-Fi', 1977);

-- Additional actors for existing movies

-- The Shawshank Redemption
INSERT INTO actors (name, movie_title) VALUES ('Morgan Freeman', 'The Shawshank Redemption');
INSERT INTO actors (name, movie_title) VALUES ('Tim Robbins', 'The Shawshank Redemption');
INSERT INTO actors (name, movie_title) VALUES ('Bob Gunton', 'The Shawshank Redemption');

-- The Dark Knight
INSERT INTO actors (name, movie_title) VALUES ('Christian Bale', 'The Dark Knight');
INSERT INTO actors (name, movie_title) VALUES ('Heath Ledger', 'The Dark Knight');
INSERT INTO actors (name, movie_title) VALUES ('Aaron Eckhart', 'The Dark Knight');

-- Inception
INSERT INTO actors (name, movie_title) VALUES ('Leonardo DiCaprio', 'Inception');
INSERT INTO actors (name, movie_title) VALUES ('Joseph Gordon-Levitt', 'Inception');
INSERT INTO actors (name, movie_title) VALUES ('Ellen Page', 'Inception');

-- Pulp Fiction
INSERT INTO actors (name, movie_title) VALUES ('John Travolta', 'Pulp Fiction');
INSERT INTO actors (name, movie_title) VALUES ('Uma Thurman', 'Pulp Fiction');
INSERT INTO actors (name, movie_title) VALUES ('Samuel L. Jackson', 'Pulp Fiction');

-- The Godfather
INSERT INTO actors (name, movie_title) VALUES ('Al Pacino', 'The Godfather');
INSERT INTO actors (name, movie_title) VALUES ('Marlon Brando', 'The Godfather');
INSERT INTO actors (name, movie_title) VALUES ('James Caan', 'The Godfather');

-- The Matrix
INSERT INTO actors (name, movie_title) VALUES ('Keanu Reeves', 'The Matrix');
INSERT INTO actors (name, movie_title) VALUES ('Laurence Fishburne', 'The Matrix');
INSERT INTO actors (name, movie_title) VALUES ('Carrie-Anne Moss', 'The Matrix');

-- Gladiator
INSERT INTO actors (name, movie_title) VALUES ('Russell Crowe', 'Gladiator');
INSERT INTO actors (name, movie_title) VALUES ('Joaquin Phoenix', 'Gladiator');
INSERT INTO actors (name, movie_title) VALUES ('Connie Nielsen', 'Gladiator');

-- Forrest Gump
INSERT INTO actors (name, movie_title) VALUES ('Tom Hanks', 'Forrest Gump');
INSERT INTO actors (name, movie_title) VALUES ('Robin Wright', 'Forrest Gump');
INSERT INTO actors (name, movie_title) VALUES ('Gary Sinise', 'Forrest Gump');

-- The Lion King
INSERT INTO actors (name, movie_title) VALUES ('Matthew Broderick', 'The Lion King');
INSERT INTO actors (name, movie_title) VALUES ('James Earl Jones', 'The Lion King');
INSERT INTO actors (name, movie_title) VALUES ('Jeremy Irons', 'The Lion King');

-- Star Wars: A New Hope
INSERT INTO actors (name, movie_title) VALUES ('Mark Hamill', 'Star Wars: A New Hope');
INSERT INTO actors (name, movie_title) VALUES ('Carrie Fisher', 'Star Wars: A New Hope');
INSERT INTO actors (name, movie_title) VALUES ('Alec Guinness', 'Star Wars: A New Hope');
