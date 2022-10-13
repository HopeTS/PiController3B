DROP TABLE IF EXISTS pin;

CREATE TABLE pin (
    pin_number INTEGER PRIMARY KEY UNIQUE NOT NULL,
    pin_name TEXT NOT NULL,
    base_type TEXT NOT NULL,
    current_type TEXT NOT NULL,
);

CREATE TABLE pin_update (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id TEXT NOT NULL,
);

