import scrapy

class ToscrapeXpathSpider(scrapy.Spider):
    name = 'toscrape-xpath'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # 使用x-path 解析response
        # /html/body/div[1]/div[2]/div[1]/div[1]

        ########.xpath("")语法#######
        # /:   从根结点查找，节点分隔符
        # nodename: 节点名字
        # //:当前位置所有子节点
        # . :选取当前节点
        # .. :当前节点的父节点
        # @属性：选择属性      //div/a/@href

        ######.xpath("")语法节点谓词操作（过滤）######
        # [1]   第1个
        # [last()] 最后一个
        # [last()-1] 倒数第二个
        # [posion()<3] 前2个
        # [@class] 有class属性的节点
        # [@class="a"] 有class属性==a的节点

        for quote in response.xpath('//div[@class="quote"]'):
            # from courses.practical_training3.quotesbot.quotesbot.items import QuotesbotItem
            # item = QuotesbotItem()
            # item["text"] = quote.xpath('./span[@class="text"]/text()').extract_first()
            # item["author"] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            # item["tags"] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            # yield item
            # 生成器 迭代
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
