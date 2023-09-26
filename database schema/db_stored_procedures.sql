
CREATE PROCEDURE registerplayer
@username varchar(255),
@password varchar(255),
@email varchar (255),
@age int,
@photo varbinary(max),
@song varbinary(max)
AS
INSERT INTO [Eagle_Defender_DB].[dbo].[player]
VALUES (@username, @password, @email, @age, @photo, @song);
GO

/*
EXEC registerplayer N'JoseA4718', N'abcd', N'jose@email.com', 23, 0x12345, 0x12345*/

CREATE PROCEDURE playerlogin
@email varchar(255),
@password varchar(255)
AS
SELECT * FROM player
WHERE player.email = @email and player.password = @password

EXEC playerlogin 'jose@email.com','acd'




