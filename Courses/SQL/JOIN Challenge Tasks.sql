
SELECT email FROM customer c
LEFT JOIN 
address a ON a.address_id = c.address_id
WHERE a.district = 'California'


SELECT f.title, a.actor_id, a.first_name, a.last_name
FROM film f
LEFT JOIN film_actor fa
ON f.film_id = fa.film_id
LEFT JOIN actor a
ON a.actor_id = fa.actor_id
WHERE a.actor_id = 2
