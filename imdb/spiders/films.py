import scrapy
from imdb.items import FilmsItem

class FilmsSpider(scrapy.Spider):
    name = "films"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    
    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        films = response.css('li.ipc-metadata-list-summary-item')
        for film in films: #on parcours chaque film 
            titre = film.css('h3.ipc-title__text::text').get()
            film_url = film.css('a::attr(href)').get() #on prend le href a chaque film
            # yield {
            #     'title': titre,
            #     'url': film_url
            # }
            
            
            yield response.follow(film_url, self.parse_product, meta = {'titre': titre})

        # #pagination
        # next_page = response.css('.page-numbers a.next::attr(href)').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse)


    #fonction est appelée pour parcourir chaque page de film. 
    def parse_product(self, response):
        titre = response.meta.get('titre')
        
        film_item = FilmsItem()

        film_item['titre'] = titre
        film_item['titre_original'] = response.css('h1 span.hero__primary-text::text').get()
        film_item['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]//span/text()').get()
        film_item['genre'] = response.css('span.ipc-chip__text::text').getall()
        film_item['year'] = response.css('a[href*="releaseinfo"]::text').get()
        film_item['duree'] = response.css('.ipc-inline-list__item::text').get()
        film_item['description'] = response.xpath('//span[@data-testid="plot-l"]/text()').get()
        film_item['acteurs'] = response.xpath('//div[@data-testid="title-cast-item"]//a[@data-testid="title-cast-item__actor"]/text()').extract()
        film_item['langue_origine'] = response.xpath('//a[contains(@class, "ipc-metadata-list-item__list-content-item") and contains(@href, "primary_language")]/text()').get()
        film_item['pays'] = response.css('li[data-testid="title-details-origin"] .ipc-metadata-list-item__list-content-item--link::text').get()
        film_item['public'] = response.css('a[href*="certificates"]::text').get()
        film_item['directeur'] = response.css('li.ipc-metadata-list__item:contains("Director") a::text').get()

        yield film_item
        
        
       