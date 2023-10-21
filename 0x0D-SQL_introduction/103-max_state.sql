-- Write a script that displays the max temperature of each state (ordered by State name).
USE hbtn_0c_0;
SOURCE /alx-higher_level_programming/0x0D-SQL_introduction/temperatures2.sql;
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
order by State;
