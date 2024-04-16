import scrapy
from imdb.items import AllocFilmsItem
import datetime
class AllocNewfilmsSpider(scrapy.Spider):
    name = "alloc_newfilms"
    allowed_domains = ["www.allocine.fr"]

    
    def start_requests(self):
        today = datetime.date.today()
        # Prochain mercredi
        next_wednesday = today + datetime.timedelta((2 - today.weekday() + 7) % 7)
        # Mercredi précédent
        last_wednesday = today - datetime.timedelta((today.weekday() - 2 + 7) % 7)

        next_wednesday_str = next_wednesday.strftime('%Y-%m-%d')
        last_wednesday_str = last_wednesday.strftime('%Y-%m-%d')

        # URL pour les films de la semaine en cours
        url_next = f"https://www.allocine.fr/film/agenda/sem-{next_wednesday_str}/"
        # URL pour les films de la semaine précédente
        url_last = f"https://www.allocine.fr/film/agenda/sem-{last_wednesday_str}/"

        yield scrapy.Request(url=url_next, callback=self.parse)
        yield scrapy.Request(url=url_last, callback=self.parse)
        
    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        films = response.css('li.mdl')
        for film in films: #on parcours chaque film 
            titre = film.css('a.meta-title-link::text').get()
            acteurs = film.css('div.meta-body-item.meta-body-actor span::text').getall() #on prend le href a chaque film
            date_sortie = film.css('div.meta-body-item.meta-body-info span::text').get()
            realisateur = film.css('div.meta-body-item.meta-body-direction span::text').getall()
            film_url = film.css('a.meta-title-link::attr(href)').get() #on prend le href a chaque film
            # yield {
            #     'title': titre,
            #     'url': film_url
            # }
            
            
            yield response.follow(film_url, self.parse_product, meta = {'titre': titre, 'acteurs': acteurs,'realisateur': realisateur, 'date_sortie':date_sortie})

        # current_page = response.meta.get('current_page', 1)
        # next_page = current_page + 1

        # if next_page <= 950:
        #     next_page_url = f"https://www.allocine.fr/films/decennie-2020/?page={next_page}"
        #     yield scrapy.Request(next_page_url, callback=self.parse, meta={'current_page': next_page})


    #fonction est appelée pour parcourir chaque page de film. 
    def parse_product(self, response):
        titre = response.meta.get('titre')
        acteurs = response.meta.get('acteurs')
        realisateur = response.meta.get('realisateur')
        date_sortie = response.meta.get('date_sortie')
        

        film_item = AllocFilmsItem()
        film_item['titre'] = titre
        film_item['duree'] =  response.css('div.meta-body-item.meta-body-info').get()
        film_item['salles'] = response.css('div.buttons-holder span.button span.txt::text').get()
        film_item['genre'] = response.css('div.meta-body-item.meta-body-info span+span+span::text').get()
        film_item['acteurs'] = acteurs
        film_item['realisateur'] = realisateur
        film_item['date_sortie'] = date_sortie
        #film_item['box_office_url'] = response.urljoin(response.css('a[title="Box Office"]::attr(href)').get())
        film_item['pays'] = response.css('section.ovw-technical .item span.nationality::text').get()
        film_item['studio'] = response.xpath("//span[contains(text(), 'Distributeur')]/following-sibling::span/text()").get()
        film_item['description'] = response.css('section.section.ovw.ovw-synopsis div.content-txt p::text').get()
        film_item['image'] = response.css('img.thumbnail-img::attr(src)').get()
        film_item['budget'] = response.xpath("//span[contains(text(), 'Budget')]/following-sibling::span/text()").get()
        film_item['entrees'] = response.xpath("//span[contains(text(), 'Box Office France')]/following-sibling::span/text()").get()
        film_item['anecdotes'] = response.xpath("//span[contains(text(), 'Secrets de tournage')]/following-sibling::span/text()").get()

        yield film_item
        