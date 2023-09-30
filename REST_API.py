import pyodbc

'''
REST API for Eagle Defender Project
Created by Jose Espinoza Chaves
'''



conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-KJ5BS8J;DATABASE=Eagle_Defender_DB;UID=access;PWD=1234;ssl=require')


def register_player(username, password, email, age, photo, song):
    try:
        cursor = conn.cursor()
        cursor.execute("EXEC registerplayer '?', '?', '?', ?, ?, ?", (username, password, email, age, photo, song))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("This user already exists, please try again", e)
        return False

register_player('JoseA4718','abcd','jose@email.com',23,'1x12443','1x857348')