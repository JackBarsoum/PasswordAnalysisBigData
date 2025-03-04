
ALTER TABLE passwords MODIFY COLUMN idpasswords TEXT CHARACTER SET utf8mb4;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/output.csv'
INTO TABLE passwords
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(passwords);

