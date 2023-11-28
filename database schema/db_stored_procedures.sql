
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
RETURNS INTEGER AS $$
DECLARE
    row_count INTEGER;
    max_entry_time integer;
BEGIN
    -- Contar el número de filas en la tabla
    SELECT COUNT(*) INTO row_count FROM leaderboard;

    -- Si la tabla tiene menos de 5 filas, simplemente inserta y devuelve 1
    IF row_count < 5 THEN
        INSERT INTO leaderboard (username, best_time, photo) VALUES (p_player_name, p_entry_time, 'NA');
        RETURN 1;
    ELSE
        -- Si la tabla ya tiene 5 filas, verifica si el nuevo tiempo es menor que el tiempo máximo actual
        SELECT MAX(best_time) INTO max_entry_time FROM leaderboard;

        IF p_entry_time < max_entry_time THEN
            -- Elimina la entrada con el tiempo más alto
            DELETE FROM leaderboard WHERE best_time = max_entry_time;
            -- Inserta la nueva entrada y devuelve 1
            INSERT INTO leaderboard (username, best_time, photo) VALUES (p_player_name, p_entry_time, 'NA');
            RETURN 1;
        ELSE
            -- Si el tiempo no es lo suficientemente bajo, no hace la inserción y devuelve 0
            RETURN 0;
        END IF;
    END IF;
END;
$$ LANGUAGE plpgsql;



insert into player(username, password, email, age, photo, song)
values ('Jose', '1234', 'jose@gmail.com', 22, 'asas', 'asasa');


select insert_leaderboard('Jose', 10)
select insert_leaderboard('Jose', 8)
select insert_leaderboard('Jose', 6)
select insert_leaderboard('Jose', 4)
select insert_leaderboard('Jose', 2)
select insert_leaderboard('Jose', 1)

select * from leaderboard;

ALTER TABLE leaderboard
ADD FOREIGN KEY (username) REFERENCES player(username);

CREATE OR REPLACE FUNCTION get_leaderboard()
RETURNS TABLE (
    username VARCHAR(255),
    best_time INTEGER,
    photo VARCHAR(255)
) AS $$
BEGIN
    RETURN QUERY
    SELECT l.username, l.best_time, l.photo
    FROM leaderboard AS l
    ORDER BY best_time ASC;
END;
$$ LANGUAGE plpgsql;

select get_leaderboard()

CREATE OR REPLACE FUNCTION check_user_limit(p_user_email varchar(255), nonvalue integer)
RETURNS INTEGER AS $$
DECLARE
    user_count INTEGER;
BEGIN
    -- Contar el número de tuplas para el usuario dado
    SELECT COUNT(*) INTO user_count
    FROM gamesxplayer
    WHERE user_email = p_user_email;

    -- Devolver 1 si ya hay 3 tuplas, 0 en caso contrario
    IF user_count = 3 THEN
        RETURN 0;
    ELSE
        RETURN 1;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insert_game_data(p_user_email varchar(255), p_game_data varchar(255))
RETURNS INTEGER AS $$
DECLARE
    user_count INTEGER;
BEGIN
    -- Contar el número de tuplas para el usuario dado
    SELECT COUNT(*) INTO user_count
    FROM gamesxplayer
    WHERE user_email = p_user_email;

    -- Verificar si el usuario ha alcanzado el límite de 3 tuplas
    IF user_count >= 3 THEN
        -- Eliminar la tupla más antigua
        DELETE FROM gamesxplayer
        WHERE (user_email, save_date) IN (
            SELECT user_email, save_date
            FROM gamesxplayer
            WHERE user_email = p_user_email
            ORDER BY save_date, CURRENT_TIME ASC
            LIMIT 1
        );
    END IF;

    -- Insertar la nueva tupla con la fecha y hora actuales
    INSERT INTO gamesxplayer (user_email, game_data, save_date)
    VALUES (p_user_email, p_game_data, NOW());

    -- Devolver 1 indicando que la inserción fue exitosa
    RETURN 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_games_by_user(p_user_email varchar(255), nonvalue integer)
RETURNS TABLE (user_email varchar(255), game_data varchar(255), save_date TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT g.user_email, g.game_data, g.save_date
    FROM gamesxplayer as g
    WHERE g.user_email = p_user_email
    ORDER BY g.save_date DESC;  -- Puedes ajustar el orden según tus necesidades
END;
$$ LANGUAGE plpgsql;
drop function get_games_by_user


select insert_game_data('marco@gmail.com','4')
select check_user_limit('jose@gmail.com')


delete from gamesxplayer

select get_games_by_user('jose@gmail.com')
select * from gamesxplayer
select * from player
alter table gamesxplayer
alter column save_date type timestamp
