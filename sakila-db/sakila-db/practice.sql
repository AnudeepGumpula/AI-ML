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






