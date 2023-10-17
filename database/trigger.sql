CREATE OR ALTER TRIGGER 
ON "public"."users-regular-season-picks"
AFTER INSERT, UPDATE, DELETE
DECLARE
    total INTEGER;
    user_id INTEGER;
    user_divisional_position INTEGER;
    

BEGIN 