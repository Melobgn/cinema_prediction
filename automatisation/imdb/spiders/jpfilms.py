import scrapy
from imdb.items import JpboxofficeItem
import re

class JpfilmsSpider(scrapy.Spider):
    name = "jpfilms"
    allowed_domains = ["www.jpbox-office.com"]
    start_urls = ["https://www.jpbox-office.com/v9_avenir.php?view=2"]

    def parse(self, response):
        # Utilisez css() pour obtenir une liste de sélecteurs pour chaque film
        movies = response.css('table.tablesmall.tablesmall3 tr')

        for movie in movies:
            # Maintenant, movie est un objet Selector et vous pouvez utiliser css() dessus
            
            entrees = movie.css('td.col_poster_contenu_majeur strong::text').get()
            new_films = JpboxofficeItem()
            new_films['entrees_premiere_semaine'] = entrees
            yield new_films
