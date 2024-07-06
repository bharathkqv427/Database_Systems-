START TRANSACTION;

-- update the product inventory
UPDATE Products SET price = price - 10 WHERE product_id = 10;

-- insert a new order
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments) values (10, 10, '2023-02-15 15:05:00', '2022-02-14', '2022-09-23', 'ordered', '519', 'wizarding hole ');
COMMIT;
START TRANSACTION;

-- update the customer's balance
UPDATE orders SET total_amount = total_amount - 50 WHERE customer_id = 3;

UPDATE orders SET status = 'ordered' WHERE order_id = 17;

COMMIT;
