from flask import Flask, request, jsonify
import psycopg2
import os
import ast
from dotenv import load_dotenv

INSERT_PLAYER = "SELECT register_player(%s, %s, %s, %s, %s, %s)"
LOGIN_PLAYER = "SELECT login_player(%s, %s)"

load_dotenv()

app = Flask(__name__)

url = os.getenv("DATABASE_URL")

# Configura la conexión a la base de datos PostgreSQL
conn = psycopg2.connect(url)

@app.post("/api/register")
def register_player():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    email = data["email"]
    age = data["age"]
    photo = data["photo"]
    song = data["song"]
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(INSERT_PLAYER, (username, password, email, age, photo, song))
            response = cursor.fetchone()[0]
            print(response)
    return response, 201

@app.post("/api/login")
def login_player():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(LOGIN_PLAYER, (email, password))
            response = cursor.fetchone()[0]
            print(response)
            if response != "(no,no,no,0,no,no)":
                # Elimina los paréntesis antes de evaluar la cadena como una tupla
                response = response.strip('()')
                # Convierte la cadena en una lista utilizando split(',')
                user_data_list = response.split(',')
                # Convierte la lista en una tupla
                user_data = tuple(user_data_list)
                # user_data ahora es una tupla con los valores de la base de datos
                '''
                user_data[0] = SINGLETONPLAYER1.username
                user_data[1] = SINGLETONPLAYER1.password
                user_data[2] = SINGLETONPLAYER1.email
                user_data[3] = SINGLETONPLAYER1.age
                user_data[4] = SINGLETONPLAYER1.photo
                user_data[5] = SINGLETONPLAYER1.song
                '''
                return {"user_data": user_data}, 201
            else:
                return {"error": "Credentials not valid"}, 401




if __name__ == '__main__':
    app.run(debug=True)