-- ADDBONUS PROCEDURE THAT INSERT DATA IN CORRECTION TABLE

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT,
							IN project_name VARCHAR(255), 
                            IN score FLOAT)
	BEGIN
    DECLARE project_id INT;
		IF(SELECT COUNT(*) FROM projects where name=project_name)=0
        THEN
			INSERT INTO projects (name) VALUES(project_name);
		END IF;
        SET project_id = (SELECT id FROM projects where name=project_name LIMIT 1);
		INSERT INTO corrections VALUES(user_id, project_id, score);
    END
$$

DELIMITER ;
