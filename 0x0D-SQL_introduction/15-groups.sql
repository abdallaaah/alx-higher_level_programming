--  lists the number of records with the same score in the table
SELECT score , COUNT(*) AS number FROM second_table group by score;
