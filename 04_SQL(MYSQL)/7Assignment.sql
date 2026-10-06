create database Company;
use Company;
create table employee(
EmpID INT PRIMARY KEY,
FirstName VARCHAR(30),
LastName VARCHAR(30),
Department  VARCHAR(30),
Salary INT,
HireDate DATE
);

INSERT INTO Employee
(EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, "Alice", "Johnson", "IT", 6500, "2020-03-15"),
(102, "Mark", "Rivera", "HR", 4800, "2019-07-22"),
(103, "Sophia", "Lee", "Finance", 7200, "2021-01-10"),
(104, "Daniel", "Kim", "IT", 5800, "2018-11-05"),
(105, "Emma", "Brown", "Marketing", 5300, "2022-04-18"),
(106, "Liam", "Patel", "Finance", 6900, "2020-09-29"),
(107, "Olivia", "Garcia", "HR", 4600, "2017-06-30"),
(108, "Noah", "Thompson", "IT", 7500, "2023-02-12"),
(109, "Ava", "Martinez", "Marketing", 5100, "2019-12-02"),
(110, "Ethan", "Davis", "Finance", 8000, "2016-05-14");

# Write a query to display every employee and all their data.
SELECT * FROM Employee;

# List only the FirstName, LastName, and Salary of every employee.
select FirstName, LastName, Salary FROM Employee;

# Show all employees who work in the 'IT' department.
Select * FROM Employee
WHERE Department="IT";

# Retrieve employees with a salary greater than 6000.
Select * from Employee
Where salary > 6000;

# List all employees ordered by HireDate from newest to oldest. 
select * from Employee
order by HireDate DESC;

# Show a list of all unique departments present in the table. 
SELECT Distinct Department from Employee;

# Find employees whose first name starts with ‘Aʼ.
SELECT * FROM Employee
WHERE FIRstName LIKE 'A%';

# Show employees whose salaries are between 4000 and 7000. 
Select salary from Employee
where salary>=4000 and salary <= 7000;

# Find the average salary of all employees.
select avg(salary) from Employee;
#or
select avg(salary) as average_salary from Employee;

# List each department along with the number of employees, but only include departments with more than 3 employees.
SELECT Department, COUNT(*) AS EmployeeCount FROM Employee
GROUP BY Department
HAVING COUNT(*) > 3;