Create database if not exists Collage_1;

Use collage_1;

create table Teacher(
id INT Primary key,
name varchar(30),
subject varchar(30),
salary INT
);

INSERT INTO Teacher
(id,name,subject, salary)
values
(23,"Ajay", "maths", 50000),
(47,"Bharat", "English", 60000),
(18, "Cheten", "Chemistry", 45000),
(9,"Divya", "Physics", 75000);

select * from Teacher;

SELECT * from Teacher
Where salary>55000;

ALTER TABLE Teacher
CHANGE salary ctc INT;

SET SQL_SAFE_UPDATES=0;
UPDATE Teacher
SET ctc=ctc+ctc*0.25;

select * from Teacher;

ALTER TABLE Teacher
ADD COLUMN city varchar(50) default "Gurgaon";

select * from Teacher;

alter table Teacher 
drop column ctc;
select * from Teacher;
