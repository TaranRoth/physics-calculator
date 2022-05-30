DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS history;

CREATE TABLE users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE history (
    username TEXT NOT NULL,
    data TEXT NOT NULL,
    time TEXT NOT NULL
);
