-- A script that lists all records of the table second_table of the database
-- in numeric order based on the score.
SELECT (score, name) FROM second_table WHERE score >= 10 ORDER BY score DESC;
