-- PROCEDURE THAT CALCULATE THE AVERAGE OF THE USER

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser ;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE USER_AVERAGE FLOAT;
    SET USER_AVERAGE = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
	UPDATE users SET average_score=USER_AVERAGE where id=user_id;
END
$$
DELIMITER ;
