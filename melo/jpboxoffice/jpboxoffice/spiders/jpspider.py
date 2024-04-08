import scrapy

from jpboxoffice.items import JpboxofficeItem


class JpspiderSpider(scrapy.Spider):
    name = "jpspider"
    allowed_domains = ["jpbox-office.com"]
    start_urls = ["https://www.jpbox-office.com/v9_demarrage.php?view=2"]
    urls_vues = set()
    custom_settings = {
    'FEEDS' : {
        'moviedata.json' : {'format' : 'json', 'overwrite' : True},
}
}
    def parse(self, response):
        movies = response.css('td.col_poster_titre')
        entrees_premiere_semaine = response.css('table.tablesmall.tablesmall5 tr td.col_poster_contenu_majeur::text').get()
        salles_premiere_semaine = response.css('table.tablesmall.tablesmall5 tr:nth-child(2) td:nth-child(7)::text').get()

        for movie in movies:
            relative_url = movie.xpath('//*[@id="content"]//td[3]/h3/a/@href').get()
            # print("Relative URL:", relative_url)
            movie_url = 'https://www.jpbox-office.com/' + relative_url

            # Vérifie si l'URL a déjà été visitée
            if movie_url in self.urls_vues:
                continue  # Passe à la prochaine URL
                
            # Ajoute l'URL à l'ensemble des URL visitées
            else:
                self.urls_vues.add(movie_url)
            yield response.follow(movie_url, callback=self.parse_movie_page, meta={'entrees_premiere_semaine' : entrees_premiere_semaine, 'salles_premiere_semaine' : salles_premiere_semaine})

        current_page = response.meta.get('current_page', 0)
        next_page = current_page + 30

        if next_page < 10000:
            next_page_url = f"https://www.jpbox-office.com/v9_demarrage.php?view=2&filtre=classg&limite={next_page}&infla=0&variable=0&tri=champ0&order=DESC&limit5=0"
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'current_page': next_page})


    def parse_movie_page(self, response):
        movie_item = JpboxofficeItem()

        entrees_premiere_semaine = response.meta.get('entrees_premiere_semaine')
        salles_premiere_semaine = response.meta.get('salles_premiere_semaine')


        movie_item['url'] = response.url
        movie_item['titre'] = response.xpath('//h1/text()').get()
        movie_item['realisateur'] = response.css('table.table_2022titre h4 a::text').get()
        movie_item['pays'] = response.css('table.table_2022titre h3 a::text').get()
        movie_item['date'] = response.xpath('//table[@class="tablelarge1"]//div//p//a/text()').get()
        movie_item['genre'] = response.css('table.table_2022titre h3 a:nth-of-type(2)::text').get()
        movie_item['studio'] = response.xpath('//h3[text()="Distribué par"]/following-sibling::text()[1]').get()
        movie_item['casting'] = response.xpath('//div[5]/div[1]/ul/li[6]/a/text()')[1].extract().strip()
        movie_item['franchise'] = response.xpath('//div[@id="nav2"]//ul//a[contains(text(), "Franchise")]/text()').get()
        movie_item['remake'] = response.xpath('//div[@id="nav2"]//ul//a[contains(text(), "Remake")]/text()').get()
        movie_item['poids_premiere_semaine'] = response.xpath("//table[contains(@class, 'tablesmall') and contains(@class, 'tablesmall2')]/tr[9]/td[3]/text()").get()
        movie_item['entrees_premiere_semaine'] = entrees_premiere_semaine
        movie_item['salles_premiere_semaine'] = salles_premiere_semaine        
        
        li5_text = response.xpath('//*[@id="nav2"]/ul/li[5]/a/text()')[-1].extract()
        li6_text = response.xpath('//*[@id="nav2"]/ul/li[6]/a/text()')[-1].extract()

        if "Casting" in li5_text:
            casting_url = response.xpath('//*[@id="nav2"]/ul/li[5]/a/@href').get()
        elif "Casting" in li6_text:
            casting_url = response.xpath('//*[@id="nav2"]/ul/li[6]/a/@href').get()
        else:
            casting_url = None

        if casting_url:
            yield response.follow(casting_url, callback=self.parse_casting, meta={'movie_item': movie_item})


        budget_url = response.xpath('//*[@id="nav2"]/ul/li[1]/a/@href').get()
        yield response.follow(budget_url, callback=self.parse_budget, meta={'movie_item' : movie_item})



    def parse_casting(self, response):
        #'response.meta' pour accéder aux métadonnées transmises
        movie_item = response.meta['movie_item']
        movie_item['acteurs'] = response.xpath('//tr[@valign="top"]/td[contains(@class, "col_poster_titre")]/h3/a[@itemprop="name"]/text()').getall()
        movie_item['producteur'] = response.xpath('//tr/td[contains(@class, "col_poster_titre") and @itemprop="producer"]/h3/a[@itemprop="name"]/text()').get()
        movie_item['compositeur'] = response.xpath('//tr/td[contains(@class, "col_poster_titre") and @itemprop="compositor"]/h3/a[@itemprop="name"]/text()').get()


    def parse_budget(self, response):
        movie_item = response.meta['movie_item']
        movie_item['budget'] = response.css('table.tablesmall.tablesmall1b tr td div strong::text').get()
        
        yield movie_item
