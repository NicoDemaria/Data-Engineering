

--Need to count the differents kinds of rating movies, below is the sql script to do the task
SELECT 
sum(CASE rating
	WHEN 'R' THEN 1
	ELSE 0
END)  R,

sum(CASE rating
	WHEN 'PG-13' THEN 1
	ELSE 0
END)  PG13 ,

sum(CASE rating
	WHEN 'PG' THEN 1
	ELSE 0
END) PG 

FROM film



