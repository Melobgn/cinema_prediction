import scrapy
from imdb.items import AllocFilmsItem

class AllocFilmsSpider(scrapy.Spider):
    name = "alloc_films"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/films/decennie-2020/"]
                #   "https://www.allocine.fr/films/pays-5001/decennie-2020/", #films en france
                #   "https://www.allocine.fr/films/pays-5002/decennie-2020/" #films aux USA
                  

    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        films = response.css('li.mdl')
        for film in films: #on parcours chaque film 
            titre = film.css('a.meta-title-link::text').get()
            acteurs = film.css('div.meta-body-item.meta-body-actor span::text').getall() #on prend le href a chaque film
            duree = film.css('div.meta-body-item.meta-body-info::text').getall() #mettre la duree
            genre = film.css('div.meta-body-item.meta-body-info span::text').getall()
            realisateur = film.css('div.meta-body-item.meta-body-direction span::text').getall()
            film_url = film.css('a.meta-title-link::attr(href)').get() #on prend le href a chaque film
            # yield {
            #     'title': titre,
            #     'url': film_url
            # }
            
            
            yield response.follow(film_url, self.parse_product, meta = {'titre': titre, 'acteurs': acteurs, 'realisateur': realisateur,'duree': duree, 'genre': genre})

        current_page = response.meta.get('current_page', 1)
        next_page = current_page + 1

        if next_page <= 950:
            next_page_url = f"https://www.allocine.fr/films/decennie-2020/?page={next_page}"
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'current_page': next_page})


    #fonction est appelée pour parcourir chaque page de film. 
    def parse_product(self, response):
        titre = response.meta.get('titre')
        acteurs = response.meta.get('acteurs')
        realisateur = response.meta.get('realisateur')
        duree = response.meta.get('duree')
        genre = response.meta.get('genre')
        
        film_item = AllocFilmsItem()
        film_item['titre'] = titre
        film_item['duree'] = duree
        film_item['genre'] = genre
        film_item['acteurs'] = acteurs
        film_item['realisateur'] = realisateur
        #film_item['box_office_url'] = response.urljoin(response.css('a[title="Box Office"]::attr(href)').get())
        film_item['pays'] = response.css('section.ovw-technical .item span.nationality::text').get()
        film_item['studio'] = response.css('section.ovw-technical .item span.blue-link::text').get()
        anecdotes = response.xpath("(//div[@class='item'])[8]/span[2]/text()").get()
        if anecdotes == "Long métrage":
            film_item['anecdotes'] = response.xpath("(//div[@class='item'])[9]/span[2]/text()").get()
        else:
            film_item['anecdotes'] = response.xpath("(//div[@class='item'])[8]/span[2]/text()").get()
            
        yield film_item
        #Long métrage
        box_office_url = response.urljoin(response.css('a[title="Box Office"]::attr(href)').get())
        if box_office_url:
            yield response.follow(box_office_url, callback=self.parse_box_office, meta={'film_item': film_item})


    def parse_box_office(self, response):
        #'response.meta' pour accéder aux métadonnées transmises
        film_item = response.meta['film_item']

        pays_box_office = response.css('h2.titlebar-title-md::text').get()

        if pays_box_office == 'Box Office France':
            premiere_entree = response.css('table.box-office-table tr.responsive-table-row:first-of-type td:nth-child(2)::text').get()
            if premiere_entree:
                premiere_entree = premiere_entree.strip().replace('\xa0', '').replace(' ', '')
                film_item['entrees'] = premiere_entree
        else:
            film_item['entrees'] = None
        yield film_item
