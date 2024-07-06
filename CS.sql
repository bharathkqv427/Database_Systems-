-- Transaction 1

START TRANSACTION;

-- Update the inventory for Product A
UPDATE Products SET count = count - 50 WHERE product_id = 99;

-- Add a new order for John Doe
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments)
VALUES (106,(SELECT customer_id FROM Customers WHERE first_name = 'Aryann'),'2023-01-11 15:04:00', '2022-02-23', '2022-09-23','ordered','51017','Metadata');
select * from orders;
COMMIT;

-- Transaction 2
START TRANSACTION;

-- Update the inventory for Product B
UPDATE Products SET count = count - 30 WHERE product_id = 100;

-- Add a new order for John Doe for Product B
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments)
VALUES (107,(SELECT customer_id FROM Customers WHERE first_name = 'Aryann'),'2023-01-11 15:04:00', '2022-02-23', '2022-09-23','ordered','51017','Metadata');
select * from orders;
COMMIT;
