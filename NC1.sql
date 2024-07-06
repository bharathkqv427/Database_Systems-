-- Transaction 1 
START TRANSACTION;
UPDATE Customers SET username = 'bruhmemer', contact_info = "387-808-6458"
WHERE customer_id= 3;
SELECT * from customers where first_name='Norman';
COMMIT;

-- Transaction 2 
START TRANSACTION;
UPDATE Customers SET username = 'high-jackman', contact_info = "424-563-4235"
WHERE customer_id = 13;
SELECT * from customer where first_name ='Atalanta';
COMMIT;