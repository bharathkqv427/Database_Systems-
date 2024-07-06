-- Transaction 1
START TRANSACTION;
UPDATE Customers SET contact_info ='161-405-1641' WHERE customer_id=4;

-- Transaction 2
START TRANSACTION;
UPDATE Customers SET contact_info ='131-305-3601' WHERE customer_id=4;

-- Commit one of the transactions
select * from Customers;
COMMIT;

-- Transaction 1
START TRANSACTION;
UPDATE Products SET stock=0 WHERE product_id=1;

-- Transaction 2
START TRANSACTION;
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments) values (118, 118, '2023-02-13 14:11:09', '2022-07-18', '2022-11-29', 'ordered', '627', 'packet applicat');

-- Commit one of the transactions
select * from Products;
select * from orders;
COMMIT;