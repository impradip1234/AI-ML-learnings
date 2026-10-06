USE instagram;

select * from users;

# updating values of followers whose age is greater than 14
UPDATE users
SET follwers=2000
WHERE age>14;

select * from users;

#Deleting some rows on the basis of condition of full table 
DELETE FROM users
WHERE follwers=123;

select * from users;

# ALTER ( TO CHANGE THE SCHEMA)
ALTER TABLE users
ADD COLUMN city VARCHAR(30) DEFAULT "Delhi";

ALTER TABLE users
DROP COLUMN city;
select * from users;

ALTER TABLE users
RENAME TO users_data;

ALTER TABLE users_data
CHANGE COLUMN follwers followers INT DEFAULT 0;

ALTER TABLE users_data
MODIFY following INT DEFAULT 5;


