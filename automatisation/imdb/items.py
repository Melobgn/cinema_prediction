# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmsItem(scrapy.Item):
    # define the fields for your item here like:
    #titre = scrapy.Field()
    titre_original = scrapy.Field()
    #score = scrapy.Field()
    genre = scrapy.Field()
    #year = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    #langue_origine = scrapy.Field()
    pays = scrapy.Field()
    public = scrapy.Field()
    image = scrapy.Field()
    realisateur = scrapy.Field()
    studio = scrapy.Field()
    date_sortie = scrapy.Field()
    budget = scrapy.Field()
   
    
class AllocFilmsItem(scrapy.Item):
    # define the fields for your item here like:
    titre = scrapy.Field()
    genre = scrapy.Field()
    #box_office_url = scrapy.Field()
    entrees = scrapy.Field()
    acteurs = scrapy.Field()
    realisateur = scrapy.Field()
    pays = scrapy.Field()
    studio = scrapy.Field()
    anecdotes = scrapy.Field()
    date_sortie = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    budget = scrapy.Field()
    duree = scrapy.Field()
    salles = scrapy.Field()
    
class JpboxofficeItem(scrapy.Item):
    entrees_premiere_semaine = scrapy.Field()
    # salles_premiere_semaine = scrapy.Field()
    # url = scrapy.Field()
    # titre = scrapy.Field()
    # realisateur = scrapy.Field()
    # pays = scrapy.Field()
    # date = scrapy.Field()
    # genre = scrapy.Field()
    # studio = scrapy.Field()
    # franchise = scrapy.Field()
    # remake = scrapy.Field()
    # acteurs = scrapy.Field()
    # producteur = scrapy.Field()
    # compositeur = scrapy.Field()
    # budget = scrapy.Field()
