-- One-to-One: A single row in one table matches exactly one row in another.
SELECT c.first_name, a.address 
FROM customer c, address a 
WHERE c.address_id = a.address_id LIMIT 5;

-- One-to-Many: One row in a table can relate to many rows in another table.
SELECT customer_id, rental_id 
FROM rental 
WHERE customer_id = 1;

-- Many-to-One: Many rows in a table point back to a single row in another table.
SELECT rental_id, staff_id 
FROM rental 
WHERE staff_id = 1;

-- Many-to-Many: Rows on both sides can relate to multiple rows on the other, linked via a bridge table.
SELECT f.title, a.first_name 
FROM film f 
JOIN film_actor fa ON f.film_id = fa.film_id JOIN actor a ON fa.actor_id = a.actor_id LIMIT 5;

-- LEFT JOIN: Returns all rows from the left table plus matches from the right, NULLs where no match.
SELECT c.customer_id, r.rental_id 
FROM customer c 
LEFT JOIN rental r ON c.customer_id = r.customer_id 
WHERE r.rental_id IS NULL;

-- RIGHT JOIN: Returns all rows from the right table plus matches from the left, NULLs where no match.
SELECT c.customer_id, r.rental_id 
FROM customer c RIGHT JOIN rental r ON c.customer_id = r.customer_id LIMIT 5;

-- FULL JOIN: Returns all rows from both tables, matched where possible (simulated in MySQL using UNION).
SELECT c.customer_id, r.rental_id 
FROM customer c LEFT JOIN rental r ON c.customer_id = r.customer_id
UNION
SELECT c.customer_id, r.rental_id 
FROM customer c RIGHT JOIN rental r ON c.customer_id = r.customer_id;

-- Cartesian Join (CROSS JOIN): Joins every row of one table with every row of another, no condition.
SELECT s.store_id, cat.name 
FROM store s CROSS JOIN category cat;

-- Subquery in SELECT: A query inside the SELECT clause that returns one value per row.
SELECT c.customer_id, (SELECT COUNT(*) FROM rental r WHERE r.customer_id = c.customer_id) AS total_rentals FROM customer c LIMIT 5;

-- Nested Queries: A query embedded inside another query's WHERE clause.
SELECT title FROM film WHERE film_id IN (SELECT film_id FROM film_category WHERE category_id = (SELECT category_id FROM category WHERE name = 'Action'));

-- Derived Table: A subquery in the FROM clause treated as a temporary table.
SELECT AVG(t.total_spent) AS avg_spend FROM (SELECT customer_id, SUM(amount) AS total_spent FROM payment GROUP BY customer_id) AS t;

-- Correlated Subquery: A subquery that references the outer query and runs once per row.
SELECT f.title FROM film f WHERE f.rental_rate > (SELECT AVG(f2.rental_rate) FROM film f2 WHERE f2.rating = f.rating);

-- CTE (Common Table Expression)
-- ============================================
-- DA temporary, named result set defined using WITH, 
-- that exists only for the duration of that one query. 
-- Makes complex queries easier to read by breaking them into steps.

WITH film_avg AS (
    SELECT AVG(rental_rate) AS avg_rate
    FROM film
)
SELECT title, rental_rate
FROM film, film_avg
WHERE film.rental_rate > film_avg.avg_rate;

-- "I calculate the average rental rate first, 
-- give that result a name (film_avg), then use it in my main query 
-- like it's a regular table."


-- VIEW

-- A saved query stored in the database as a virtual 
-- table. Doesn't store data itself — it runs the underlying query 
-- fresh every time you SELECT from it. Persists until you DROP it.

CREATE VIEW active_customers AS
SELECT customer_id, first_name, last_name, email
FROM customer
WHERE active = 1;

-- can use it like a normal table:
SELECT * FROM active_customers;

-- "A view is like a saved shortcut for a query I use 
-- often. Instead of retyping the same WHERE conditions every time, 
-- I query the view directly."


-- ============================================
-- TEMPORARY TABLE
-- ============================================
-- A real table that stores actual data, but only exists 
-- for the duration of your session/connection. Automatically 
-- deleted when the session ends. Useful for holding intermediate 
-- results you'll query multiple times.

CREATE TEMPORARY TABLE temp_customer_totals AS
SELECT customer_id, SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id;

-- Now query it like any table, as many times as needed:
SELECT * FROM temp_customer_totals WHERE total_spent > 100;
SELECT AVG(total_spent) FROM temp_customer_totals;

-- A temporary table actually stores the data 
-- (unlike a view), but only for my current session. It's useful 
-- when I need to reuse the same intermediate results multiple 
-- times without recalculating them each time.


-- ============================================
-- STORED PROCEDURE
-- ============================================
-- A saved block of SQL code (can include logic, 
-- variables, conditions) that you can call by name, as many times 
-- as needed, with or without parameters.

DELIMITER //

CREATE PROCEDURE GetCustomersByStore(IN store_num INT)
BEGIN
    SELECT customer_id, first_name, last_name
    FROM customer
    WHERE store_id = store_num;
END //

DELIMITER ;

-- Call it whenever needed, passing in different values:
CALL GetCustomersByStore(1);
CALL GetCustomersByStore(2);

-- A stored procedure is like a saved function — 
-- I write the logic once, and then just call it with different 
-- inputs whenever I need it, instead of rewriting the whole query.


-- Practice: Keys & Indexes

-- Q1: Identify the surrogate key in the customer table, and write a query that retrieves customers using it.
SELECT customer_id, first_name, last_name
FROM customer
WHERE customer_id = 5;
-- customer_id is the surrogate key: auto-generated, no real-world meaning.


-- Q2: Identify a possible natural key in the customer table, and write a query that retrieves a customer using it instead.
SELECT customer_id, first_name, last_name, email
FROM customer
WHERE email = 'MARY.SMITH@sakilacustomer.org';
-- email is a natural key candidate: real-world data that could (in theory) uniquely identify a customer.


-- Q3: Create an index on the film table's title column, since it's commonly searched/filtered on.
CREATE INDEX idx_film_title ON film(title);

-- Now test that a title search can use this index:
SELECT * FROM film WHERE title = 'ACADEMY DINOSAUR';


-- Q4: Create an index on the customer table's last_name column.
CREATE INDEX idx_customer_lastname ON customer(last_name);

SELECT * FROM customer WHERE last_name = 'SMITH';


-- Q5: Check which indexes already exist on the customer table.
SHOW INDEX FROM customer;
-- Notice: customer_id (primary key) is already indexed automatically, since it's the clustered index.


-- Q6: Check which indexes already exist on the film table.
SHOW INDEX FROM film;


-- Q7: Identify the clustered index of the rental table (this will be the primary key by default in InnoDB).
SHOW INDEX FROM rental WHERE Key_name = 'PRIMARY';


-- Q8: Create a composite (multi-column) non-clustered index on payment table's customer_id and payment_date, 
-- since queries often filter by both together.
CREATE INDEX idx_payment_customer_date ON payment(customer_id, payment_date);

-- Test it with a query that uses both columns:
SELECT * FROM payment 
WHERE customer_id = 5 AND payment_date >= '2005-05-01';


-- Q9: Drop an index you created (cleanup / practice reversing it).
DROP INDEX idx_film_title ON film;


-- Q10: Use EXPLAIN to see whether a query uses an index or does a full table scan.
EXPLAIN SELECT * FROM customer WHERE last_name = 'SMITH';
-- Check the 'key' column in the output — if it shows idx_customer_lastname, the index is being used. 
-- If it says NULL, MySQL did a full table scan instead.


-- Q11: Compare EXPLAIN output for a column WITHOUT an index, to see the performance difference conceptually.
EXPLAIN SELECT * FROM customer WHERE first_name = 'MARY';
-- first_name has no index, so this likely does a full table scan (unless MySQL decides otherwise based on table size/stats).


-- Q12: Identify why customer_id is a better primary/surrogate key than email, by testing what happens if email format changes.

-- If a customer's email changes, customer_id stays the same, so all foreign key references (in rental, payment, etc.) remain valid.
-- If email were used as the key instead, every related table would need updating whenever the email changes — this is why 
-- surrogate keys are preferred for primary keys in practice.




