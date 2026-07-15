-- Assignment: CTE, Views, Temporary Tables, Stored Procedures


-- Q1-Q5: SUBQUERIES

-- Q1: Display all customer details who have made more than 5 payments.
SELECT *
FROM customer c
WHERE (
    SELECT COUNT(*) 
    FROM payment p 
    WHERE p.customer_id = c.customer_id
) > 5;


-- Q2: Find the names of actors who have acted in more than 10 films.
SELECT first_name, last_name
FROM actor a
WHERE (
    SELECT COUNT(*) 
    FROM film_actor fa 
    WHERE fa.actor_id = a.actor_id
) > 10;


-- Q3: Find the names of customers who never made a payment.
SELECT first_name, last_name
FROM customer c
WHERE c.customer_id NOT IN (
    SELECT DISTINCT customer_id 
    FROM payment
);


-- Q4: List all films whose rental rate is higher than the 
-- average rental rate of all films.
SELECT title, rental_rate
FROM film
WHERE rental_rate > (
    SELECT AVG(rental_rate) 
    FROM film
);


-- Q5: List the titles of films that were never rented.
SELECT title
FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT i.film_id
    FROM inventory i
    WHERE i.inventory_id IN (
        SELECT DISTINCT rental.inventory_id FROM rental
    )
);


-- Q6-Q7: VIEWS

-- Q6: Display the customers who rented films in the same month 
-- as customer with ID 5.

-- Step 1: Create a view showing customer_id with rental month/year
CREATE VIEW customer_rental_months AS
SELECT customer_id,
       MONTH(rental_date) AS rental_month,
       YEAR(rental_date) AS rental_year
FROM rental;

-- Step 2: Use the view to find customers who rented in the same 
-- month/year as customer 5
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM customer c
JOIN customer_rental_months crm ON c.customer_id = crm.customer_id
WHERE (crm.rental_month, crm.rental_year) IN (
    SELECT rental_month, rental_year
    FROM customer_rental_months
    WHERE customer_id = 5
)
AND c.customer_id <> 5;


-- Q7: Find all staff members who handled a payment greater than the average payment amount.

-- Step 1: Create a view showing average payment amount
CREATE VIEW avg_payment_view AS
SELECT AVG(amount) AS avg_amount
FROM payment;

-- Step 2: Use the view to filter staff who handled above-average payments
SELECT DISTINCT s.staff_id, s.first_name, s.last_name
FROM staff s
JOIN payment p ON s.staff_id = p.staff_id
WHERE p.amount > (SELECT avg_amount FROM avg_payment_view);



-- Q8-Q9: CTE (Common Table Expressions)

-- Q8: Show the title and rental duration of films whose rental duration is greater than the average.

WITH avg_duration AS (
    SELECT AVG(rental_duration) AS avg_rental_duration
    FROM film
)
SELECT f.title, f.rental_duration
FROM film f, avg_duration ad
WHERE f.rental_duration > ad.avg_rental_duration;


-- Q9: Find all customers who have the same address as customer with ID 1.

WITH target_address AS (
    SELECT address_id
    FROM customer
    WHERE customer_id = 1
)
SELECT c.customer_id, c.first_name, c.last_name
FROM customer c, target_address ta
WHERE c.address_id = ta.address_id
  AND c.customer_id <> 1;


-- Q10: STORED PROCEDURE

-- Q10: List all payments that are greater than the average 
-- of all payments.

DELIMITER //

CREATE PROCEDURE GetAboveAveragePayments()
BEGIN
    DECLARE avg_amt DECIMAL(10,2);
    
    SELECT AVG(amount) INTO avg_amt FROM payment;
    
    SELECT payment_id, customer_id, staff_id, amount, payment_date
    FROM payment
    WHERE amount > avg_amt;
END //

DELIMITER ;

-- Call the procedure to run it:
CALL GetAboveAveragePayments();