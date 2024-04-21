def scoring_casting(film, actors_df):
    poids_total = 0
    noms_personnes_dans_film = ','.join(film['acteurs'] + film['realisateurs'])
    for personne in noms_personnes_dans_film.split(','):
        if personne in actors_df['name'].values:
            poids_acteur = actors_df.loc[actors_df['name'] == personne, 'coef_personne'].values[0]
            poids_total += poids_acteur
    return poids_total


def get_studio_coefficient(studio, conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                CASE
                    WHEN studio IN ('Walt Disney Pictures','Warner Bros.','Paramount','Sony Pictures','Universal','20th Century Fox','Lionsgate','Columbia') THEN 3
                    WHEN studio IN ('Pathé','Studiocanal','Gaumont','UGC Distribution','SND','Le Pacte','Metropolitan','EuropaCorp','GBVI','Wild Bunch','UFD','ARP Selection','Ad vitam','Haut et Court','Films du Losange','Rezo Films','TFM Distribution') THEN 2
                    WHEN studio IN ('Gébéka','Memento Films','KMBO','Océan Films','AMLF','MK2 Diffusion','Gaumont Sony','Apollo Films','Sophie Dulac','Eurozoom','Jour2Fête','Pan-Européenne','Cinema Public','Polygram') THEN 1
                    ELSE 0
                END AS studio_coefficient
            FROM
                films
            WHERE
                studio = %s
        """, (studio,))
        studio_coef = cursor.fetchone()[0]
        cursor.close()
        return studio_coef
    except mysql.connector.Error as e:
        print(f"Erreur lors de l'exécution de la requête SQL: {e}")
        return 0  


