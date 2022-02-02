import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://www.midsouthshooterssupply.com/item/00129ae224vlk1/224-valkyrie-75-grain-total-metal-jacket-20-rounds/']

    def parse(self, response):
        for ele in response.css('main .page-wrap'):
            yield{
                'name of product': ele.css(' .product-heading .product-name::text').get(),
                'product price': ele.css(' .product-info .price strike::text').get(),
                'sale price': ele.css(' .product-info .price .whatadeal::text').get(),
                'Status': ele.css(' .product-info .status .in-stock::text').get(),
                'manufacture': ele.css(' #description b::text')[1].get()

            }
        next_product = response.css(
            ' .related-items .lSSlideWrapper li .product a::attr(href) ').get()

        if next_product is not None:
            url = 'https://www.midsouthshooterssupply.com' + next_product

            yield scrapy.Request(url, callback=self.parse)
