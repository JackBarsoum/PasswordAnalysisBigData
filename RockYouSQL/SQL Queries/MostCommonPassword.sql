SELECT passwords.passwords, COUNT(*) AS Frequency
FROM passwords.passwords
GROUP BY passwords.passwords
ORDER BY Frequency DESC
LIMIT 1; 



