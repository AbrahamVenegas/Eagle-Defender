from flask import Flask, request, jsonify
import psycopg2
import os
import re
import json
from dotenv import load_dotenv

INSERT_PLAYER = "SELECT register_player(%s, %s, %s, %s, %s, %s)"
LOGIN_PLAYER = "SELECT login_player(%s, %s)"
GET_LEADERBOARD = "SELECT get_leaderboard()"
INSERT_LEADERBOARD = "SELECT insert_leaderboard(%s, %s)"
CHECK_SAVE_LIMIT = "SELECT check_user_limit(%s)"
SAVE_GAME = "SELECT insert_game_data(%s, %s)"
GET_SAVED_GAMES = "SELECT get_games_by_user(%s, %s)"

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

@app.post("/api/loginp1")
def login_player_1():
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
                data = {
                    "username": user_data[0],
                    "password": user_data[1],
                    "email": user_data[2],
                    "age": user_data[3],
                    "photo": user_data[4],
                    "song": user_data[5],
                }
                jsonRoute = "json/player1.json"
                with open(jsonRoute, 'w') as f:
                    json.dump(data, f)

                return {"user_data": user_data}, 201
            else:
                return {"error": "Credentials not valid"}, 401

@app.post("/api/loginp2")
def login_player_2():
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
                data = {
                    "username": user_data[0],
                    "password": user_data[1],
                    "email": user_data[2],
                    "age": user_data[3],
                    "photo": user_data[4],
                    "song": user_data[5],
                }
                jsonRoute = "json/player2.json"
                with open(jsonRoute, 'w') as f:
                    json.dump(data, f)

                return {"user_data": user_data}, 201
            else:
                return {"error": "Credentials not valid"}, 401


@app.get("/api/getleaderboard")
def get_leaderboard():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_LEADERBOARD)
            response = cursor.fetchall()

            # Procesar las cadenas manualmente
            leaderboard_data = []
            for tupla_str, in response:
                # Eliminar paréntesis y comillas
                clean_str = tupla_str.strip("()'")
                # Dividir por comas y obtener los elementos
                elements = clean_str.split(",")
                nombre = elements[0]
                numero = int(elements[1])
                leaderboard_data.append((nombre, numero, 'NA'))
            return leaderboard_data


@app.post("/api/insertleaderboard")
def insert_leaderboard(username, time):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(INSERT_LEADERBOARD, (username, time))
            response = cursor.fetchall()
            if response[0][0] == 1:
                print('True')
                return True
            else:
                print('False')
                return False

@app.post("/api/checksavelimit")
def check_save_limit(email):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CHECK_SAVE_LIMIT, email)
            response = cursor.fetchall()
            if response[0][0] == 1:
                print('True')
                return True
            else:
                print('False')
                return False

@app.post("/api/savegame")
def save_game(email, game_json):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SAVE_GAME, (email, game_json))
            response = cursor.fetchall()
            if response[0][0] == 1:
                print('True')
                return True
            else:
                print('False')
                return False

@app.post("/api/getplayersaves")
def get_player_saves(email, nonvalue):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(GET_SAVED_GAMES, (email, nonvalue))
            response = cursor.fetchall()

            processed_data = []
            for tupla_str, in response:
                # Dividir la cadena en tres partes: email, game_info, timestamp
                elements = tupla_str.split(",", 2)
                email = elements[0].strip("()")
                # Eliminar las comillas y los backslashes del JSON
                json_str = elements[1].replace("\\", "").strip('"')
                timestamp = elements[2].strip("()")
                processed_data.append((email, json_str, timestamp))
            print(processed_data)
            return processed_data



if __name__ == '__main__':
    app.run(debug=True)
