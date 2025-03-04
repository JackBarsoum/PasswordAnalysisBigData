SELECT lENGTH(idpasswords) AS PasswordLengths, COUNT(*) AS Frequency
FROM bigdata.passwords 
GROUP BY PasswordLengths 
ORDER BY PasswordLengths;