CREATE DATABASE kino;
USE kino;

CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomi VARCHAR(100)
);

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomi VARCHAR(100),
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

INSERT INTO genres (nomi)
VALUES
('Fantastika'),
('Komediya'),
('Jangari'),
('Drama');

INSERT INTO movies (nomi, genre_id)
VALUES
('Avatar', 1),
('Mr Bean', 2),
('John Wick', 3),
('Titanic', 4);

SELECT movies.nomi, genres.nomi AS janr
FROM movies
JOIN genres ON movies.genre_id = genres.id;