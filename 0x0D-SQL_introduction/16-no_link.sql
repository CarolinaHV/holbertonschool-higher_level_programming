-- This script lists all records of the table second_table
-- of the database hbtn_0c_0 in MySQL server.
INSERT INTO `second_table` (`score`, `name`) VALUES ("12", "Aria");
INSERT INTO `second_table` (`score`, `name`) VALUES ("18", "Aria");
SELECT score, name FROM second_table WHERE score >= 10
       ORDER BY score DESC, name;
