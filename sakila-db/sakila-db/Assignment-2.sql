-- Assignment 2

-- Q1: Identify if there are duplicates in Customer table  (without using customer_id)

SELECT first_name,
       last_name,
       email,
       address_id,
       COUNT(*) AS duplicate_count
FROM customer
GROUP BY first_name, last_name, email, address_id
HAVING COUNT(*) > 1;


-- Q2: Number of times letter 'a' is repeated in film descriptions
SELECT SUM(
         LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'a', ''))
       ) AS total_a_count
FROM film;


-- Q3: Number of times each vowel is repeated in film descriptions
SELECT 
    SUM(LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'a', ''))) AS count_a,
    SUM(LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'e', ''))) AS count_e,
    SUM(LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'i', ''))) AS count_i,
    SUM(LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'o', ''))) AS count_o,
    SUM(LENGTH(LOWER(description)) - LENGTH(REPLACE(LOWER(description), 'u', ''))) AS count_u
FROM film;


-- Q4: Display the payments made by each customer

-- 4a. Month wise
SELECT customer_id,
       YEAR(payment_date) AS payment_year,
       MONTH(payment_date) AS payment_month,
       SUM(amount) AS total_amount
FROM payment
GROUP BY customer_id, YEAR(payment_date), MONTH(payment_date)
ORDER BY customer_id, payment_year, payment_month;

-- 4b. Year wise
SELECT customer_id,
       YEAR(payment_date) AS payment_year,
       SUM(amount) AS total_amount
FROM payment
GROUP BY customer_id, YEAR(payment_date)
ORDER BY customer_id, payment_year;

-- 4c. Week wise
SELECT customer_id,
       YEAR(payment_date) AS payment_year,
       WEEK(payment_date) AS payment_week,
       SUM(amount) AS total_amount
FROM payment
GROUP BY customer_id, YEAR(payment_date), WEEK(payment_date)
ORDER BY customer_id, payment_year, payment_week;


-- Q5: Check if any given year is a leap year or not 
-- (hardcoded date, no Sakila table)
SELECT 2024 AS year_checked,
       CASE 
           WHEN (2024 % 4 = 0 AND 2024 % 100 <> 0) OR (2024 % 400 = 0)
           THEN 'Leap Year'
           ELSE 'Not a Leap Year'
       END AS leap_year_status;


-- Q6: Display number of days remaining in the current year from today
SELECT CURDATE() AS today,
       DATEDIFF(CONCAT(YEAR(CURDATE()), '-12-31'), CURDATE()) AS days_remaining_in_year;


-- Q7: Display quarter number (Q1, Q2, Q3, Q4) for payment dates 
-- from payment table
SELECT payment_id,
       payment_date,
       CONCAT('Q', QUARTER(payment_date)) AS payment_quarter
FROM payment;