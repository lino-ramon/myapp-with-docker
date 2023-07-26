CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase

CREATE TABLE IF NOT EXISTS products (
    id INT(11) AUTO_INCREMENT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    PRIMARY KEY (id)
);

INSERT INTO products (id, name, price) 
VALUES
    (0, 'Notebook Dell Inspiron 5000', 2700),
    (0, 'Samsung Galaxy S20FE', 2200);