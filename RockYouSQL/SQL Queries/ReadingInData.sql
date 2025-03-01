
ALTER TABLE passwords MODIFY COLUMN passwords TEXT CHARACTER SET utf8mb4;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/rockyou_clean.txt'
INTO TABLE passwords
CHARACTER SET utf8mb4
FIELDS TERMINATED BY '\n'
LINES TERMINATED BY '\n'
(passwords);

