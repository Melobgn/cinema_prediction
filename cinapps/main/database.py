import mysql.connector
import os

def connect_to_azure_mysql():
    try:
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        host = os.getenv('HOST')
        database = os.getenv('DATABASE')
        #print(user)
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database)
        if conn.is_connected():
            print('Connecté à la base de données MySQL Azure')
            return conn
    except mysql.connector.Error as e:
        print(f"Erreur de connexion à la base de données MySQL: {e}")
