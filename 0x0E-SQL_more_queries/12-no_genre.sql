-- 11. Genre ID for all shows
SELECT t.title, g.genre_id
FROM tv_shows AS t 
LEFT JOIN tv_show_genres AS g ON g.show_id = t.id
WHERE g.genre_id IS NULL
ORDER BY g.show_id, t.id ASC;
