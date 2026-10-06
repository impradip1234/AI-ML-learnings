create table customers(
customer_id INT primary key,
name varchar(30),
city varchar(30)
);
create table orders(
order_id INT,
customer_id INT,
amount INT
);

INSERT INTO customers
(customer_id, name, city)
values
(1, "Alice", "Mumbai"),
(2, "Bob", "Delhi"),
(3, "Charlie", "Bangalore"),
(4, "David", "Mumbai");

INSERT INTO orders
(order_id, customer_id, amount)
values
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);


#Inner Join 

SELECT * 
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

#left join

select * 
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id;

# Right join 

select * 
from customers c
right join orders o
on c.customer_id=o.customer_id;

#outer join

select * from customers as c
left join orders as o
on c.customer_id=o.customer_id
UNION
select * from customers as c
right join orders as o
on c.customer_id=o.customer_id;

# cross join 
select * from customers 
cross join orders;

#self join 

select * from customers as a
join customers as b
on a.customer_id=b.customer_id;

# left exclisive join
select * from customers as c
left join orders as o
on c.customer_id=o.customer_id
Where o.customer_id is null;

# right exclusive join
select * from customers as c
right join orders as o
on c.customer_id=o.customer_id
 where c.customer_id is null;