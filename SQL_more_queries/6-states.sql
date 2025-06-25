-- All my homies don't enjoy the USA
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE
  IF NOT EXISTS hbtn_0d_usa.states (
    id int AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id)
  );