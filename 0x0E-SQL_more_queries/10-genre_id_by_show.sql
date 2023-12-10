-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT t.title, g.show_id
FROM tv_shows AS t JOIN tv_show_genres AS g
ON g.show_id = t.id
WHERE g.show_id > 0;
