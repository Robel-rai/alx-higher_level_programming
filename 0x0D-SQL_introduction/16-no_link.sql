-- Lists all recoreds on the base
SELECT score, name FROM second_table 
WHERE name IS NOT NULL ORDER BY score DESC;
