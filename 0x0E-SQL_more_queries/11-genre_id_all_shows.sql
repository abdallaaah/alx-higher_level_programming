-- 11. Genre ID for all shows
SELECT t.title, g.genre_id
FROM tv_shows AS t RIGHT JOIN tv_show_genres AS g
ON g.show_id = t.id
ORDER BY t.title, g.genre_id ASC;
