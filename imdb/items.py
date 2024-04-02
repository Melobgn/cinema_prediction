# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmsItem(scrapy.Item):
    # define the fields for your item here like:
    titre = scrapy.Field()
    titre_original = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    year = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    langue_origine = scrapy.Field()
    pays = scrapy.Field()
    public = scrapy.Field()
    directeur = scrapy.Field()

class AllocFilmsItem(scrapy.Item):
    # define the fields for your item here like:
    titre = scrapy.Field()
    duree = scrapy.Field()
    genre = scrapy.Field()
    #box_office_url = scrapy.Field()
    entrees = scrapy.Field()
    acteurs = scrapy.Field()
    realisateur = scrapy.Field()
    pays = scrapy.Field()
    studio = scrapy.Field()
    anecdotes = scrapy.Field()