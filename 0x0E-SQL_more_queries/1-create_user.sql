-- This script creates the MySQL user user_0d_1
-- with all privileges given to it.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1-pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d-1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
