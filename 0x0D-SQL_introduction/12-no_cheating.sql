-- This script updates the score of
-- Bob to 10 in the table second_table
UPDATE second_table SET score = (SELECT 10 LIMIT 1) WHERE name = 'Bob'
