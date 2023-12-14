-- TRIGGER THAT CHECK EMAIL ON UPDATE EVENT

DROP TRIGGER IF EXISTS before_update_on_email;
DELIMITER $$

CREATE TRIGGER before_update_on_email
BEFORE UPDATE ON users  FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email
    THEN
    SET NEW.valid_email = 0;
    END IF;
END
$$
DELIMITER ;
