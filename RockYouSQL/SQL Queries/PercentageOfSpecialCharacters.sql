SELECT (Count(*) / (SELECT Count(*) 
FROM passwords.passwords))*100 
FROM passwords.passwords
WHERE passwords.passwords REGEXP '[^a-zA-Z0-9\n\r[:space:]]';