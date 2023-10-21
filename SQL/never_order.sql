select c.name as Customers
from customers c left join orders o
on c.id = o.customerID
where customerID is NULL;

-- LINK : https://leetcode.com/problems/customers-who-never-order/