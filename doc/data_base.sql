CREATE TABLE movie(
    code VARCHAR(10) NOT NULL,
    name VARCHAR(1000) NOT NULL,
    image_url VARCHAR(255),
    year int(4),
    CONSTRAINT code_pk PRIMARY KEY (code)
);

CREATE TABLE review(
    id int(8) AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    description VARCHAR(4000) NOT NULL,
    rating int(1) NOT NULL,
    code VARCHAR(10) NOT NULL,
    CONSTRAINT id_pk PRIMARY KEY(id),
    CONSTRAINT review_movie_pk FOREIGN KEY(code) REFERENCES movie(code)
);