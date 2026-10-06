use company;

DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT salary
    from employee
    where EmpID=acc_id;
END $$
DELIMITER ;

CALL check_balance(1);
DROP PROCEDURE IF EXISTS check_salary;

DELIMITER $$
CREATE PROCEDURE check_salary(IN Emp_id INT)
BEGIN
	SELECT Salary FROM employee
    Where EmpID=Emp_id;
END $$
DELIMITER ;
CALL check_salary(102);


# creating procedure to give input EmpID and get OUTPUT FirstName
DELIMITER ##
CREATE PROCEDURE check_name(IN emp_id INT, OUT Name varchar(30))
BEGIN
	SELECT FirstName INTO Name
    from employee
    where EmpID=emp_id;
END ##
DELIMITER ;

CALL check_name(103, @Name_of_employee);
select @Name_of_employee;
