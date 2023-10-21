-- Import in hbtn_0c_0 database this table dump: download
USE hbtn_0c_0;
SOURCE /alx-higher_level_programming/0x0D-SQL_introduction/temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM `temperatures` GROUP BY city order by avg_temp desc;
