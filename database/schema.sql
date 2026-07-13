CREATE TABLE users(
id INTEGER PRIMARY KEY,
name TEXT,
income FLOAT,
risk TEXT
);

CREATE TABLE investments(
id INTEGER PRIMARY KEY,
user_id INTEGER,
amount FLOAT
);
