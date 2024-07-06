START TRANSACTION;

-- Update the quantity of a product in the inventory
UPDATE products
SET count = count - 2
WHERE product_id = 2;

-- Insert a new order for a customer
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments) values (113, 113, now(), now(), now(), 'ordered', '519', 'plankton raise');
select * from orders;
COMMIT;

START TRANSACTION;


-- Update the customer's address
UPDATE Customers
SET username = 'vip'
WHERE customer_id = 100;

select * from Customers;
COMMIT;