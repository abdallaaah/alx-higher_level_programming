-- Number of shows by genre
SELECT t.name AS genre, COUNT(g.genre_id) AS number_of_shows
FROM tv_genres AS t JOIN tv_show_genres AS g
ON t.id = g.genre_id
GROUP BY t.name
ORDER BY number_of_shows DESC;
