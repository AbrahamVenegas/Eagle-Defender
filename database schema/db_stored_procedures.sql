
CREATE OR REPLACE FUNCTION register_player(
username_in varchar,
password_in varchar,
email_in varchar,
age_in integer,
photo_in varchar,
song_in varchar)
RETURNS varchar as $$
DECLARE
	resultado varchar;
BEGIN
	BEGIN
		INSERT INTO player (username, password, email, age, photo, song)
		VALUES (username_in, password_in, email_in, age_in, photo_in, song_in);
		resultado := 'done';
	EXCEPTION
		WHEN others THEN 
			resultado := 'error';
	END;
	RETURN resultado;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION login_player(
    email_in text,
    pass_in text
) 
RETURNS TABLE (username varchar, password varchar, email varchar, age integer, photo varchar, song varchar) AS $$
BEGIN
    RETURN QUERY
    SELECT * 
	FROM player 
	WHERE player.email = email_in 
	AND player.password = pass_in;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM player
DROP FUNCTION login_player
SELECT login_player('jose@email.com','abcd')


