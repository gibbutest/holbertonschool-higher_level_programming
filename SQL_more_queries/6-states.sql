-- All my homies don't enjoy the USA
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

use hbtn_0d_usa;

CREATE TABLE
  IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
  );