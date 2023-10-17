CREATE TRIGGER update_regular_season_score
AFTER UPDATE
ON "public"."users-regular-season-picks"

    
BEGIN 

    DECLARE
    current_year INTEGER := 2023
    total INTEGER
    username TEXT


    FOR id IN (SELECT id, username FROM "public"."users") LOOP
        total := 0
        SELECT u.username INTO username
        FROM "public"."users" AS u
        WHERE u.id = id.id;
        RAISE NOTICE 'Processing user: %', username

        FOR team_name, team_division, division_position, year IN (SELECT * FROM "public"."users-regular-season-picks" WHERE user_id = id.id AND year = current_year) LOOP
            SELECT 
                team_name, team_division, division_position 
            FROM 
                "public"."nfl-seasons" as s
            WHERE s.team_name = team_name.team_name AND s.year = year.year;
            
            -- Check if division positions are equal and increment total
            IF s.division_position = division_position THEN
                total := total + 1;
            END IF;

            RAISE NOTICE 'Team: %, Division Position: %', team_name, division_position
        END

        -- You can now use the 'total' variable for this user

        -- UPDATE OR INSERT STATEMENT

        -- END UPDATE OR INSERT
    END LOOP;

    RAISE NOTICE 'Final Total for User %: %', username, total; -- Add a notice for final total
    -- Use 'total' outside the loop for the final result
END;