-- No genres!
SELECT
  tv_shows.title,
  tv_show_genres.genre_id
FROM
  tv_shows
  LEFT JOIN tv_show_genres on tv_show_genres.show_id = tv_shows.id
WHERE
  tv_show_genres.genre_id IS NULL
ORDER BY
  tv_shows.title ASC,
  tv_show_genres.genre_id ASC;