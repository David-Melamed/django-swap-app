-- create database
CREATE DATABASE IF NOT EXISTS my_application;

-- create the user
CREATE USER 'admin' IDENTIFIED BY 'password';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON `my_application`.* TO 'admin'@'%';

FLUSH PRIVILEGES;