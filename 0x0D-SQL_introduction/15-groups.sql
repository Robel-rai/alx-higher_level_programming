-- listes the amount of number similar scores appered and diplays them in the given oreder.
SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC;
