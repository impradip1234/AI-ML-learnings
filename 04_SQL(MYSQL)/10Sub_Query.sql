use prime;

#  with WHERE.........
select * 
from orders
where amount>(
select avg(amount)
from orders);

# With SELECT 
SELECT name,
    (select COUNT(*)
    FROM orders o
    WHERE o.customer_id=c.customer_id
    ) as order_count
FROM  customers c;

# With FROM

SELECT summary.customer_id, summary.avg_amount
FROM 
	(
		SELECT customer_id, AVG(amount) as avg_amount
		FROM orders
		GROUP BY customer_id
	)as summary;
    
# creating view 
CREATE VIEW view1 as 
SELECT customer_id, name FROM customers;

select * from view1;

# creating index....
CREATE INDEX inded_branch ON customers(city);
DROP INDEX inded_branch ON customers;
SHOW INDEX FROM customers;
select * from customers
where city= "Mumbai";


