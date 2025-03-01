SELECT lENGTH(passwords) AS PasswordLengths, COUNT(*) AS Frequency
FROM passwords.passwords 
GROUP BY PasswordLengths 
ORDER BY PasswordLengths;
