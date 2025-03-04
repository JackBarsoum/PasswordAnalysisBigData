SELECT (Count(*) / (SELECT Count(*) 
FROM bigdata.passwords))*100 
FROM bigdata.passwords
WHERE passwords.idpasswords REGEXP '[^a-zA-Z0-9\n\r[:space:]]';