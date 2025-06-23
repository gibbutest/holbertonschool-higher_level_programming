-- Say. My. Name.... You're god damn right!
SELECT
  score,
  name
FROM
  second_table
WHERE
  name IS NOT NULL
ORDER BY
  score DESC;