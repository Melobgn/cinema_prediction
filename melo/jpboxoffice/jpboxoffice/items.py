# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JpboxofficeItem(scrapy.Item):
    url = scrapy.Field()
    titre = scrapy.Field()
    realisateur = scrapy.Field()
    pays = scrapy.Field()
    date = scrapy.Field()
    genre = scrapy.Field()
    studio = scrapy.Field()
    casting = scrapy.Field()
    franchise = scrapy.Field()
    remake = scrapy.Field()
    nombre_entrees_premiere_semaine = scrapy.Field()
    nombre_salles_premiere_semaine = scrapy.Field()
    poids_premiere_semaine = scrapy.Field()
    acteurs = scrapy.Field()
    producteur = scrapy.Field()
    compositeur = scrapy.Field()
