CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 0ef44ead5916

CREATE TABLE plays (
    id SERIAL NOT NULL, 
    title VARCHAR NOT NULL, 
    writer VARCHAR NOT NULL, 
    director VARCHAR NOT NULL, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_plays_id ON plays (id);

CREATE TABLE users (
    id SERIAL NOT NULL, 
    username VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    password VARCHAR NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (email), 
    UNIQUE (username)
);

CREATE INDEX ix_users_id ON users (id);

CREATE TABLE reviews (
    id SERIAL NOT NULL, 
    user_id INTEGER NOT NULL, 
    play_id INTEGER NOT NULL, 
    content VARCHAR NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(play_id) REFERENCES plays (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE INDEX ix_reviews_id ON reviews (id);

INSERT INTO alembic_version (version_num) VALUES ('0ef44ead5916') RETURNING alembic_version.version_num;

