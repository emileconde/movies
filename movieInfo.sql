CREATE DATABASE IF NOT EXISTS movie_info;

USE movie_info;

CREATE TABLE IF NOT EXISTS movie_data(
    id INT(8),
    title VARCHAR(255),
    overview VARCHAR(255),
    popularity FLOAT(8,2),
    backdrop_path VARCHAR(255),
    poster_path VARCHAR(255),
    release_date VARCHAR(255)
)