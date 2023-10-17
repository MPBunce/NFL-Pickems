CREATE OR ALTER TRIGGER 
ON "public"."users-regular-season-picks"
AFTER INSERT, UPDATE, DELETE
DECLARE
    current_year INTEGER := 2023;
    total INTEGER := 0;
    user_id INTEGER;
    user_divisional_position INTEGER;
    
BEGIN 

    FOR id IN (SELECT * FROM "public"."users-regular-season-picks" WHERE year = 2023 AND userId = id )LOOP