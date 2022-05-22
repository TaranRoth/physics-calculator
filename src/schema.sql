DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS history;

CREATE TABLE users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE history (
    user_id INTEGER NOT NULL,
    data BLOB NOT NULL,
    time INTEGER NOT NULL

);
