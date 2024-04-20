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


def calculate_score(person, influential_df):
    if person in influential_df['name'].values:
        row = influential_df[influential_df['name'] == person]
        score = (row['nombre_tournage'].values[0] + row['prix'].values[0]) / row['duree_carriere'].values[0]
        return score
    return 0

def update_prediction_scores(films, influential_df):
    for film in films:
        actors_score = sum(calculate_score(actor, influential_df) for actor in film['acteurs'])
        directors_score = sum(calculate_score(director, influential_df) for director in film['realisateurs'])
        film['scoring_acteurs_realisateurs'] = actors_score + directors_score
    return films