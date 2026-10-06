--- Table Queries
CREATE DATABASE IF NOT EXISTS instagram;
USE instagram;
# create table 
CREATE TABLE users(
id INT PRIMARY KEY,
age INT,
name VARCHAR(30) NOT NULL,
email VARCHAR(30) UNIQUE,
follwers INT DEFAULT 0,
following INT DEFAULT 0,
CONSTRAINT age_check CHECK (age>=13)
#PRIMARY KEY (id)
);

CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(100),
user_id INT,
FOREIGN KEY (user_id) REFERENCES users(id)
);

# insert data in table 
INSERT INTO users
(id,age,name,email,follwers, following)
VALUES
(1,14,"adam","adam@gmail.com",123,145),
(2,15,"bob","bob@gmail.com",345, 2545),
(3,35,"Pradip","pradipyadav@gmail.com",345,445);
#Select * from users;  --- to see the table....

#SELECT COMMAND....
SELECT id,name,email FROM users;
SELECT * FROM users;
SELECT DISTINCT age FROM users;

#WHERE clauses 
SELECT * FROM users
WHERE age BETWEEN 15 AND 17 AND follwers>200;

SELECT name,follwers FROM users
WHERE follwers >=134;

SELECT * FROM users
WHERE email NOT IN ("pradipyadav@gmail.com","bob@gmail.com");

SELECT * FROM users
WHERE age>=13
LIMIT 2;

SELECT * FROM users
ORDER BY follwers DESC;

SELECT max(follwers)
FROM users;

SELECT min(follwers)
FROM users;

SELECT count(age) 
FROM users 
WHERE age>13;

SELECT sum(follwers)
FROM users;

SELECT avg(follwers)
FROM users;

SELECT age, max(follwers)
FROM users
GROUP BY age;V 

SELECT age, max(follwers)
FROM users
GROUP BY ages
HAVING age>14;

SELECT age, max(follwers)
FROM users
WHERE age>13
GROUP BY age
HAVING age<100
ORDER BY age DESC;
