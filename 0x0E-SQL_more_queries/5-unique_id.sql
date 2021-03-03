-- This script creates the table unique_id on MySQL server.
-- with id INT with the default value 1 and must be unique and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1,
       name VARCHAR(256),
       UNIQUE KEY (id)
);
