CREATE DATABASE IF NOT EXISTS book_database

CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    isbn TEXT);

