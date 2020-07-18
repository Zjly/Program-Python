import logging

import scrapy

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        list_movie = response.xpath("//div[@class='item']")
        for item in list_movie:
            from courses.practical_training3.douban.douban.items import MovieItem
            movie = MovieItem()
            movie["rank"] = item.xpath("div[@class='pic']/em/text()").extract()
            movie["title"] = item.xpath("div[@class='info']/div[@class='hd']/a/span[@class='title'][1]/text()").extract()
            yield movie