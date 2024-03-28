-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert all tables in the database to utf8mb4
SELECT CONCAT('ALTER TABLE ', table_name, ' CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0';
