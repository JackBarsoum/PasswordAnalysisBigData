SELECT (Count(*) / (SELECT Count(*) 
FROM passwords.passwords))*100 
FROM passwords.passwords
WHERE passwords.passwords REGEXP '[0-9]';

