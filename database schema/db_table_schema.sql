-- Database: EagleDefenderDB

-- DROP DATABASE IF EXISTS "EagleDefenderDB";

CREATE DATABASE "EagleDefenderDB"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Canada.1252'
    LC_CTYPE = 'English_Canada.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
CREATE TABLE player(
username VARCHAR(255) UNIQUE,
password VARCHAR(255),
email varchar(255) PRIMARY KEY,
age integer,
photo varchar(255),
song varchar(255)
);

CREATE TABLE gamesxplayer(
user_email varchar(255),
game_data varchar(255),
save_date date
);

CREATE TABLE leaderboard(
username varchar(255),
best_time time,
photo varchar(255)
);


ALTER TABLE gamesxplayer
ADD FOREIGN KEY (user_email) REFERENCES player(email);

ALTER TABLE leaderboard
ADD FOREIGN KEY (username) REFERENCES player(username);