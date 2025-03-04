SELECT (Count(*) / (SELECT Count(*) 
FROM bigdata.passwords))*100 
FROM bigdata.passwords
WHERE passwords.idpasswords REGEXP '[0-9]';

