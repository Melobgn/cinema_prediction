def get_directors_by_film(conn, film_id):
    """
    Fetches a list of directors associated with a given film from the database.
    Args:
    conn: MySQL database connection object.
    film_id: ID of the film for which directors are to be fetched.
    
    Returns:
    A list of dictionaries containing director details.
    """
    directors = []
    query = """
    SELECT p.id_personne, p.nom 
    FROM Personnes p
    JOIN Participations part ON p.id_personne = part.id_personne
    JOIN Films f ON part.id_film = f.id_film
    WHERE f.id_film = %s AND part.role = 'realisateur';
    """
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (film_id,))
        directors = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error fetching directors: {e}")
    return directors

def get_actors_by_film(conn, film_id):
    """
    Fetches a list of actors associated with a given film from the database.
    Args:
    conn: MySQL database connection object.
    film_id: ID of the film for which actors are to be fetched.
    
    Returns:
    A list of dictionaries containing actor details.
    """
    actors = []
    query = """
    SELECT p.id_personne, p.nom 
    FROM Personnes p
    JOIN Participations part ON p.id_personne = part.id_personne
    JOIN Films f ON part.id_film = f.id_film
    WHERE f.id_film = %s AND part.role = 'acteur';
    """
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (film_id,))
        actors = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"Error fetching actors: {e}")
    return actors
