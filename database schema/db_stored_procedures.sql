
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
DECLARE
    user_exists boolean;
BEGIN
    -- Verificar si el usuario existe
    SELECT EXISTS (SELECT 1 FROM player WHERE player.email = email_in AND player.password = pass_in) INTO user_exists;

    -- Si el usuario existe, devolver la información del usuario; si no, devolver valores predeterminados
    IF user_exists THEN
        RETURN QUERY
        SELECT * FROM player WHERE player.email = email_in AND player.password = pass_in;
    ELSE
        RETURN QUERY
        SELECT 'no'::varchar, 'no'::varchar, 'no'::varchar, 0, 'no'::varchar, 'no'::varchar;
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM player
DROP FUNCTION login_player
SELECT login_player('jose@email.com','abcd')

CREATE OR REPLACE FUNCTION insert_leaderboard(p_player_name VARCHAR(255), p_entry_time integer)
RETURNS VOID AS $$
DECLARE
    row_count INTEGER;
    max_entry_time integer;
BEGIN
    -- Contar el número de filas en la tabla
    SELECT COUNT(*) INTO row_count FROM leaderboard;

    -- Si la tabla tiene menos de 5 filas, simplemente inserta
    IF row_count < 5 THEN
        INSERT INTO leaderboard (username, best_time, photo) VALUES (p_player_name, p_entry_time, 'NA');
    ELSE
        -- Si la tabla ya tiene 5 filas, verifica si el nuevo tiempo es menor que el tiempo máximo actual
        SELECT MAX(best_time) INTO max_entry_time FROM leaderboard;

        IF p_entry_time < max_entry_time THEN
            -- Elimina la entrada con el tiempo más alto
            DELETE FROM leaderboard WHERE best_time = max_entry_time;
            -- Inserta la nueva entrada
            INSERT INTO leaderboard (username, best_time, photo) VALUES (p_player_name, p_entry_time, 'NA');
        END IF;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE RULE maximo_cinco_filas_rule
AS ON INSERT TO leaderboard
DO INSTEAD (
    SELECT contar_filas();
    INSERT INTO leaderboard VALUES (NEW.*);
);

insert into player(username, password, email, age, photo, song)
values ('Jose', '1234', 'jose@gmail.com', 22, 'asas', 'asasa');

select insert_leaderboard('Jose', 10)

ALTER TABLE leaderboard
ALTER COLUMN best_time TYPE INTEGER USING EXTRACT(EPOCH FROM best_time)::INTEGER;

