#checking autocommint status
SELECT @@autocommit;
#Seting off the autocommit
SET autocommit=0;
create database prime;
use prime;
create table accounts(
id INT primary key AUTO_INCREMENT,
name varchar(50),
balance DECIMAL(10,2)
);
INSERT INTO accounts(name, balance) values
("Pradip",300.00),
("Aditya",500.00),
("Satish",1000.00);
select * from accounts;

START TRANSACTION;
UPDATE accounts set balance=balance-50 where id=1;
UPDATE accounts set balance=balance+50 where id=2;
COMMIT;

SELECT * FROM accounts;

START TRANSACTION;
UPDATE accounts set balance=balance-50 where id=1;
UPDATE accounts set balance=balance+50 where id=2;
ROLLBACK;

SELECT * FROM accounts;

START TRANSACTION;
UPDATE accounts SET balance= balance+1000 where id=1;
SAVEPOINT after_topup;
UPDATE accounts SET balance= balance+10 where id=2;
ROLLBACK to after_topup;
COMMIT;