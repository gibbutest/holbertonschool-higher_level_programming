-- All the genres
SELECT
  tv_genres.name as genre,
  COUNT(tv_show_genres.show_id) as number_of_shows
FROM
  tv_genres
  LEFT JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY
  tv_genres.id
HAVING
  COUNT(tv_show_genres.show_id > 0)
ORDER BY
  number_of_shows DESC;