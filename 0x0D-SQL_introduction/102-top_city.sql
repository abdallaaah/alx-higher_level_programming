-- Write a script that displays the top 3 of cities temperature during July and August
USE hbtn_0c_0;
SOURCE /alx-higher_level_programming/0x0D-SQL_introduction/temperatures1.sql;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7,8)
GROUP BY city
order by avg_temp desc
LIMIT 3;
