SELECT passwords.idpasswords, COUNT(*) AS Frequency
FROM bigdata.passwords
GROUP BY passwords.idpasswords
ORDER BY Frequency DESC
LIMIT 1; 



