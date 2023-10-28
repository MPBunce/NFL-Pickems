CREATE OR REPLACE PROCEDURE public.update_regular_season_scores(p_year int)
LANGUAGE plpgsql
AS $$
DECLARE
    rec record;
    score int;
BEGIN
    FOR rec IN 
        SELECT id, username FROM "public"."users"
    LOOP
        -- Initialize the score for each user
        score := 0;
		
        SELECT 
            SUM(
                CASE 
                    WHEN "nfl-seasons"."divisional_position" = "users-regular-season-picks"."division_position" THEN 1
                    ELSE 0
                END
            ) INTO score
        FROM "nfl-seasons"
        INNER JOIN "users-regular-season-picks" ON "nfl-seasons".team_name = "users-regular-season-picks".team_name
        WHERE "nfl-seasons".year = p_year AND "users-regular-season-picks".user_id = rec.id;

        RAISE INFO 'User ID: %, Username: %, Matches: %', rec.id, rec.username, score;
		
		
		
        -- Insert or update the user's score in the "users-scores" table
        INSERT INTO public."users-scores" (username, year, regular_season_score)
        VALUES (rec.username, p_year, score)
        ON CONFLICT (username, year)
        DO UPDATE
        SET regular_season_score = EXCLUDED.regular_season_score;		
		
		
		
    END LOOP;
END;
$$;


CALL public.update_regular_season_scores(2023);