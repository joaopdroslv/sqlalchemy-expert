CREATE DATABASE IF NOT EXISTS cinema;

USE cinema;

CREATE TABLE IF NOT EXISTS movies (
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(128) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (title)
);

-- Inserting data into the 'movies' table
INSERT INTO movies (title, genre, year) VALUES ('Forest Gump', 'Drama', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Matrix', 'Sci-Fi', 1999);
INSERT INTO movies (title, genre, year) VALUES ('Inception', 'Sci-Fi', 2010);
INSERT INTO movies (title, genre, year) VALUES ('The Godfather', 'Crime', 1972);
INSERT INTO movies (title, genre, year) VALUES ('Pulp Fiction', 'Crime', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Shawshank Redemption', 'Drama', 1994);
INSERT INTO movies (title, genre, year) VALUES ('The Dark Knight', 'Action', 2008);
INSERT INTO movies (title, genre, year) VALUES ('The Lord of the Rings: The Return of the King', 'Fantasy', 2003);
INSERT INTO movies (title, genre, year) VALUES ('Fight Club', 'Drama', 1999);
INSERT INTO movies (title, genre, year) VALUES ('Forrest Gump', 'Drama', 1994);
INSERT INTO movies (title, genre, year) VALUES ('Star Wars: Episode IV - A New Hope', 'Sci-Fi', 1977);
INSERT INTO movies (title, genre, year) VALUES ('The Terminator', 'Action', 1984);
INSERT INTO movies (title, genre, year) VALUES ('Gladiator', 'Action', 2000);
INSERT INTO movies (title, genre, year) VALUES ('Interstellar', 'Sci-Fi', 2014);
INSERT INTO movies (title, genre, year) VALUES ('The Lion King', 'Animation', 1994);
