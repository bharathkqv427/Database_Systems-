-- Transaction 1: 
START TRANSACTION;
UPDATE Products SET count = count - 7 WHERE product_id = 5;
COMMIT;

-- Transaction 2: 
START TRANSACTION;
UPDATE Products SET count = count  - 9 WHERE product_id = 5;
COMMIT;