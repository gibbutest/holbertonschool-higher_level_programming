-- Beans
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

use hbtn_0d_usa;

CREATE TABLE
  IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
  );

CREATE TABLE
  IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL
  );

ALTER TABLE cities ADD CONSTRAINT fk_cities_state FOREIGN KEY (state_id) REFERENCES states (id);