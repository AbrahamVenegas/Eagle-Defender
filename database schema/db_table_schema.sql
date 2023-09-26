CREATE TABLE player(
	username VARCHAR(255) UNIQUE,
	password VARCHAR(255),
	email varchar(255) PRIMARY KEY,
	age integer,
	photo varbinary(max),
	song varbinary(max)
	);

CREATE TABLE gamesxplayer(
user_email varchar(255),
game_data varchar(max),
save_date date

);

CREATE TABLE leaderboard(
username varchar(255),
best_time time,
photo varbinary(max)
);