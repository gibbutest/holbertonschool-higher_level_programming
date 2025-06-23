-- Only the best of the best. Men in Black, in Black?
SELECT
  score,
  name
FROM
  second_table
WHERE
  score >= 10
ORDER BY
  score DESC;