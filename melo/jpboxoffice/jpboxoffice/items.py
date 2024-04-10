# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JpboxofficeItem(scrapy.Item):
    entrees_premiere_semaine = scrapy.Field()
    salles_premiere_semaine = scrapy.Field()
    url = scrapy.Field()
    titre = scrapy.Field()
    realisateur = scrapy.Field()
    duree = scrapy.Field()
    pays = scrapy.Field()
    date = scrapy.Field()
    genre = scrapy.Field()
    studio = scrapy.Field()
    franchise = scrapy.Field()
    remake = scrapy.Field()
    acteurs = scrapy.Field()
    producteur = scrapy.Field()
    compositeur = scrapy.Field()
    budget = scrapy.Field()
