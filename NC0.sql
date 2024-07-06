START TRANSACTION;

insert into Products (category_id, product_id, p_name, count, price, description, stock, manf_date, expiry_date) values (96, 103, 'Loin feather', 200, 460, "it was just a lion feather" , 'available', '2018-03-27', '2023-11-22');

-- Update the inventory for Product A
UPDATE Products SET count = count - 50 WHERE product_id = 103;


insert into Customers (customer_id, first_name, last_name, username, password, contact_info) values (109, 'Aryann', 'malik', 'staffe0', 'fffdPaRLs', '161-435-1671');

-- Add a new order for John Doe
insert into orders (order_id, customer_id, ordered_date, req_date, shipping_date, status, total_amount, comments)
VALUES (104,(SELECT customer_id FROM Customers WHERE first_name = 'Aryann'),'2023-01-11 15:04:00', '2022-02-23', '2022-09-23','ordered','51017','Metadata');

COMMIT;
