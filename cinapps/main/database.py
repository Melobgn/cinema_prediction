import mysql.connector

def connect_to_azure_mysql():
    try:
        conn = mysql.connector.connect(
            user='Spies',
            password='Simplon1948',
            host='dbcinapps.mysql.database.azure.com',
            database='dbcinapps')
        if conn.is_connected():
            print('Connecté à la base de données MySQL Azure')
            return conn
    except mysql.connector.Error as e:
        print(f"Erreur de connexion à la base de données MySQL: {e}")
