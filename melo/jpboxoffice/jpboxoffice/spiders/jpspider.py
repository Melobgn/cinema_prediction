import scrapy

from jpboxoffice.items import JpboxofficeItem


class JpspiderSpider(scrapy.Spider):
    name = "jpspider"
    allowed_domains = ["jpbox-office.com"]
    start_urls = ["https://www.jpbox-office.com/v9_demarrage.php?view=2"]

    custom_settings = {
    'FEEDS' : {
        'moviedata.json' : {'format' : 'json', 'overwrite' : True},
}
}
    def parse(self, response):
        movies = response.css('td.col_poster_titre')
        for movie in movies:
            relative_url = movie.xpath('//*[@id="content"]//td[3]/h3/a/@href').get()
            # print("Relative URL:", relative_url)
            movie_url = 'https://www.jpbox-office.com/' + relative_url
            yield response.follow(movie_url, callback=self.parse_movie_page)

        current_page = response.meta.get('current_page', 0)
        next_page = current_page + 30

        if next_page < 10000:
            next_page_url = f"https://www.jpbox-office.com/v9_demarrage.php?view=2&filtre=classg&limite={next_page}&infla=0&variable=0&tri=champ0&order=DESC&limit5=0"
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'current_page': next_page})


    def parse_movie_page(self, response):
        movie_item = JpboxofficeItem()

        movie_item['url'] = response.url
        movie_item['name'] = response.xpath('//h1/text()').get()
        # movie_item['years_career'] = response.xpath('//*[@id="content-layout"]/div[2]/div/section[1]/div/div[2]/div[1]/div[1]/text()').get()
        # movie_item['number_films_series'] = response.xpath('//*[@id="content-layout"]/div[2]/div/section[1]/div/div[2]/div[2]/div[1]/text()').get()

        yield movie_item