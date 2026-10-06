use collage_1;
CREATE TABLE Student(
roll_no INT primary key,
name varchar(30),
city varchar(30),
marks int);

INSERT INTO Student
(roll_no, name, city, marks)
values
(110,"adam", "Delhi", 75),
(108, "Bob", "Mumbai", 65),
(124, "Casey", "Pune", 94),
(112, "Duke", "PUne", 80);

select * from Student 
where marks >75;

select distinct city
from Student;
---or 
select city 
from Student 
group by city;

select city, max(marks) from Student
group by city;


select avg(marks) 
from Student;

alter table Student
add column grade varchar(1);

update Student 
set grade="O"
where marks>80;

update student 
set grade="A"
where marks>=70 and marks<=80;


update Student 
set grade="B"
where marks>=60 and marks<=70;
select * from Student;