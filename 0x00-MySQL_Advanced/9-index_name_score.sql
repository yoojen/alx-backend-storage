-- CREATED INDEX N MULTIPLE COLUMNS IN THE SAME TABLE

CREATE INDEX idx_name_first_score
ON names (name(1), score);
