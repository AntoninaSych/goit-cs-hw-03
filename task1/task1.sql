-- Створення таблиці users
CREATE TABLE users (
                       id SERIAL PRIMARY KEY,
                       fullname VARCHAR(100) NOT NULL,
                       email VARCHAR(100) UNIQUE NOT NULL
);

-- Створення таблиці status
CREATE TABLE status (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) UNIQUE NOT NULL
);

-- Вставка початкових значень у таблицю status
INSERT INTO status (name) VALUES
                              ('new'),
                              ('in progress'),
                              ('completed');

-- Створення таблиці tasks
CREATE TABLE tasks (
                       id SERIAL PRIMARY KEY,
                       title VARCHAR(100) NOT NULL,
                       description TEXT,
                       status_id INTEGER NOT NULL,
                       user_id INTEGER NOT NULL,
                       CONSTRAINT fk_status
                           FOREIGN KEY(status_id)
                               REFERENCES status(id),
                       CONSTRAINT fk_user
                           FOREIGN KEY(user_id)
                               REFERENCES users(id)
                               ON DELETE CASCADE
);
