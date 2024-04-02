import scrapy


class WikiFilmsSpider(scrapy.Spider):
    name = "wiki_films"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["https://fr.wikipedia.org/wiki/Liste_de_films_ayant_fait_le_plus_d%27entr%C3%A9es_en_premi%C3%A8re_semaine_en_France"]

    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque films
    #pour obtenir plus de détails.
    def parse(self, response):
        films = response.css('tr')
        for film in films: #on parcours chaque film 
            titre = film.css('tr i a::text').get()
            film_url = film.css('tr i a::attr(href)').get() #on prend le href a chaque film
            entries = film.xpath('.//td/following-sibling::td[3]/text()').get()
            pays = film.xpath('.//span[@class="datasortkey"]/a/@title').get()
            # yield {
            #     'title': titre,
            #     'url': film_url,
            #     'entries': entries,
            #     'pays': pays
            # }
            if film_url is None:
                film_url = 'Non spécifié'
                
            yield response.follow(film_url, self.parse_product, meta = {'titre': titre, 'entries':entries, 'pays': pays})

        # #pagination
        # next_page = response.css('.page-numbers a.next::attr(href)').get()
        # if next_page:
        #     yield response.follow(url=next_page, callback=self.parse)


    #fonction est appelée pour parcourir chaque page de film. 
    def parse_product(self, response):
        titre = response.meta.get('titre')
        entries = response.meta.get('entries')
        pays = response.meta.get('pays')
        
        yield {
                'title': titre,
                'entries': entries,
                'pays': pays
            }
        
        
        # film_item = FilmsItem()

        # film_item['titre'] = titre
        # film_item['score'] = response.xpath('//div[@data-testid="hero-rating-bar__aggregate-rating__score"]//span/text()').get()
        # film_item['genre'] = response.css('span.ipc-chip__text::text').getall()
