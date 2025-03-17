import scrapy


class WhiskeySpider(scrapy.Spider):
    name='whisky'
    start_urls=['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self,response):
        
        for products in response.css('div.product-item-info'):
            try:
           
                yield {
                    'name': products.css('a.product-item-link::text').get() ,
                    'price': products.css('span.price::text').get() ,
                    'link' : products.css('a.product-item-link::attr(href)').get()
                }
            except:

                    yield {
                    'name': products.css('a.product-item-link::text').get() ,
                    'price': "sold out",
                    'link' : products.css('a.product-item-link::attr(href)').get()
                }
                    

        next_page = response.css('a.action.next::attr(href)').get()
        if next_page is not None:
             yield response.follow(next_page,callback=self.parse)